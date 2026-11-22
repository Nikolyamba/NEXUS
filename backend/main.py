from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from backend.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
