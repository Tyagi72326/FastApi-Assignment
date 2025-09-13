
from fastapi import FastAPI
from .routes import router
from .crud import create_index_if_not_exists

app = FastAPI(title="Employee Management")

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await create_index_if_not_exists()
