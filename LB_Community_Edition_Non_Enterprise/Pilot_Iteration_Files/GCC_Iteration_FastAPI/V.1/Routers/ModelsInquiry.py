from typing import List
import os
from pathlib import Path
import inspect
from sqlalchemy.orm.decl_api import DeclarativeMeta

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
            classes = []
            
            for name, obj in inspect.getmembers(module, lambda x: inspect.isclass(x) and issubclass(x, DeclarativeMeta)):
                classes.append(name)
            
            models.append({"module_name": module_name, "classes": classes})
        
        except Exception as e:
            models.append({"module_name": module_name, "error": str(e)})
    
    return models
