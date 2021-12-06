from fastapi import FastAPI
from fastapi import APIRouter
from .produtc.views import router as product_router


router = APIRouter()

router.include_router(product_router, prefix='/product')