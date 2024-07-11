from fastapi import FastAPI, Query
from typing import List, Dict
from pydantic import BaseModel, Field
from pathlib import Path
import inspect
from Config import Database  # Import Database from Config module
from Routers.ModelsInquiry import get_model_names  # Import get_model_names from Routers.ModelsInquiry module

app = FastAPI()

# Example BaseModel class to represent model fields and types with metadata
class ModelField(BaseModel):
    name: str = Field(..., title="Field Name", description="Name of the field")
    type: str = Field(..., title="Field Type", description="Type of the field")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Endpoint to get all model names with detailed information
@app.get("/models", response_model=List[Dict[str, List[ModelField]]])
async def get_all_models() -> List[Dict[str, List[ModelField]]]:
    """
    Retrieve all model names and their fields from the 'Models' directory.
    """
    package_path = Path(__file__).parent / "Models"
    model_files = [f.stem for f in package_path.glob("*.py") if f.name != '__init__.py']

    models_info = []

    for model_file in model_files:
        module_name = f"Models.{model_file}"
        try:
            module = __import__(module_name, fromlist=[""])
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and obj.__module__ == module_name:
                    model_info = {"module_name": module_name, "class_name": name, "fields": []}
                    for field_name, field_type in obj.__annotations__.items():
                        model_info["fields"].append({"name": field_name, "type": str(field_type)})
                    models_info.append(model_info)
        except Exception as e:
            models_info.append({"module_name": module_name, "error": str(e)})

    # Convert field info to ModelField objects
    models_info_with_model_fields = []
    for model_info in models_info:
        fields = model_info.pop("fields")
        model_fields = [ModelField(name=field["name"], type=field["type"]) for field in fields]
        models_info_with_model_fields.append({**model_info, "fields": model_fields})

    return models_info_with_model_fields
