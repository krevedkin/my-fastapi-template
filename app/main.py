from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.session import db_helper


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=settings.run.reload)
