from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import SessionLocal
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from app.security import verify_token
import logging
from redis import Redis
from app.redis_client import redis_instance
from app.config import get_settings
from app.security import get_current_user
from fastapi import HTTPException
from app.models import UserRoles

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Security(oauth2_scheme)):
    user = verify_token(token)  # Example function to verify token
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user


async def check_admin_user(user: UserRoles = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient privileges")
    return user

# Usage in router:
# dependencies=[Depends(check_admin_user)]

async def get_config():
    return get_settings()

# Usage in router:
# dependencies=[Depends(get_config)]


def get_redis():
    try:
        yield redis_instance
    finally:
        # Optionally, close or release resources related to Redis connection
        pass

# Usage in router:
# dependencies=[Depends(get_redis)]




logger = logging.getLogger(__name__)
async def log_request(request: Request):
    logger.info(f"Request received: {request.url}")
    return request





def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
