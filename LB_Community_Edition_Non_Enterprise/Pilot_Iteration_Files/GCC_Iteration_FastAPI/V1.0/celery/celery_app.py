from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "main",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["tasks.tasks"]  # Adjust this as needed
)

celery_app.conf.update(
    result_expires=3600,
)
