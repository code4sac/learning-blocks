from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import os
import inspect
from Config import Database


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}




# Function to get all model names from models directory
def get_model_names(models_package: str) -> List[dict]:
    models = []
    
    # Construct full path to models_package directory
    package_path = os.path.join(os.path.dirname(__file__), models_package.replace(".", os.path.sep))
    
    # Get list of files in models_package directory
    model_files = [f[:-3] for f in os.listdir(package_path) if f.endswith('.py') and f != '__init__.py']
    
    # Import each module dynamically
    for model_file in model_files:
        module_name = f"{models_package}.{model_file}"
        try:
            module = __import__(module_name, fromlist=[""])
        except ImportError as e:
            continue
        
        # Collect class names
        classes = []
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and obj.__module__ == module_name:
                classes.append(name)
        
        models.append({"module_name": module_name, "classes": classes})
    
    return models

# Endpoint to get all model names with detailed information
@app.get("/models", response_model=List[dict])
async def get_all_models():
    package_path = os.path.join(os.path.dirname(__file__), "Models")
    model_files = [f[:-3] for f in os.listdir(package_path) if f.endswith('.py') and f != '__init__.py']

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