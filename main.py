from contextlib import asynccontextmanager
from fastapi import FastAPI
from connection import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    

app = FastAPI(lifespan=lifespan)

from routers import user

app.include_router(user.router)
