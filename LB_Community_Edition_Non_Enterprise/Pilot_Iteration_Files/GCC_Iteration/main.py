# app/main.py
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import os
import inspect

app = FastAPI()

# Function to get all model names from models directory
def get_model_names(models_package: str) -> List[str]:
    models = []
    
    # Get list of files in models_package directory
    model_files = [f[:-3] for f in os.listdir(models_package) if f.endswith('.py') and f != '__init__.py']
    
    # Import each module dynamically
    for model_file in model_files:
        module_name = f"{models_package}.{model_file}"
        module = __import__(module_name, fromlist=[""])
        
        # Iterate over members of the module
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj != BaseModel:
                models.append(name)
    
    return models

# Endpoint to get all model names
@app.get("/models", response_model=List[str])
async def get_all_models():
    return get_model_names("app.models")

@app.get("/")
def read_root():
    return {"Hello": "World"}
