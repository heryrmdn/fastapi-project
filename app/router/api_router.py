from fastapi import APIRouter
from app.router.product_router import product_router

prefix = "/api/v1"
api_router = APIRouter()
api_router.include_router(product_router, prefix=prefix)