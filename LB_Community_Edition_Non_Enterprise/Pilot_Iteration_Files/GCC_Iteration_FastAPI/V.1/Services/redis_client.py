import redis
from app.core.config import settings  # Adjust the import according to your project structure

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    db=0
)

def get_redis_client():
    return redis_client
