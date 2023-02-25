from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/calculate")
async def calculate():
    # Your Python script logic here
    result = 1 + 2
    return {"result": result}

app.include_router(router)
