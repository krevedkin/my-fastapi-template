from fastapi import APIRouter
from app.api.api_v1.endpoints import foo

api_router = APIRouter()


api_router.include_router(foo.router, prefix="/foo", tags=["foo"])
