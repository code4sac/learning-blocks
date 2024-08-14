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

"""
from fastapi import FastAPI, Request, HTTPException, Depends
from typing import List, Dict
from pydantic import BaseModel, Field
from pathlib import Path
import inspect
import asyncio
from aioredis import Redis, create_redis_pool
from config.RedisConfig import REDIS_CONFIG  # Import Redis configuration

app = FastAPI()

# Example BaseModel class to represent model fields and types with metadata
class ModelField(BaseModel):
    name: str = Field(..., title="Field Name", description="Name of the field")
    type: str = Field(..., title="Field Type", description="Type of the field")

# Redis client setup (using aioredis)
async def get_redis(redis_config: dict = REDIS_CONFIG) -> Redis:
    redis = await create_redis_pool(f'redis://{redis_config["host"]}:{redis_config["port"]}')
    return redis

# Root endpoint
@app.get("/")
async def read_root(request: Request, redis: Redis = Depends(get_redis)):
    ip_address = request.client.host  # Get client IP address from request
    cached_data = await redis.get(f'ip:{ip_address}')
    if cached_data:
        return {"message": "Hello, World!", "cached_ip_address": cached_data.decode()}
    else:
        await redis.set(f'ip:{ip_address}', ip_address)
        return {"message": "Hello, World!", "ip_address": ip_address}

# Endpoint to get all model names with detailed information
@app.get("/models", response_model=List[Dict[str, List[ModelField]]]])
async def get_all_models(request: Request, redis: Redis = Depends(get_redis)) -> List[Dict[str, List[ModelField]]]]:
    """
    Retrieve all model names and their fields from the 'Models' directory.
    """
    ip_address = request.client.host  # Get client IP address from request
    cached_data = await redis.get(f'ip:{ip_address}')
    if cached_data:
        return {"message": "Hello, World!", "cached_ip_address": cached_data.decode()}
    else:
        await redis.set(f'ip:{ip_address}', ip_address)
        return {"message": "Hello, World!", "ip_address": ip_address}

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

"""
