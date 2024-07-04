
from typing import List
import inspect

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
