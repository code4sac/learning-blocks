from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pathlib import Path
import inspect
from Config import Database  # Ensure this is correct
from Routers.ModelsInquiry import get_model_names  # Ensure this is correct

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Endpoint to get all model names with detailed information
@app.get("/models", response_model=List[dict])
async def get_all_models():
    package_path = Path(__file__).parent / "Models"
    model_files = [f.stem for f in package_path.glob("*.py") if f.name != '__init__.py']

    models = []

    for model_file in model_files:
        module_name = f"Models.{model_file}"
        try:
            module = __import__(module_name, fromlist=[""])
            classes = []
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and obj.__module__ == module_name:
                    classes.append(name)
            models.append({"module_name": module_name, "classes": classes})
        except Exception as e:
            models.append({"module_name": module_name, "error": str(e)})

    return models
