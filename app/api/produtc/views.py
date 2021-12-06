from fastapi import APIRouter, status
from fastapi import Depends
from app.api.repositories.product_repository import ProductRepository
from app.models.models import Product
from .schemas import ProductSchema, ShowproductSchema 
from typing import List

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def creat(product: ProductSchema, repository: ProductRepository = Depends()):
    repository.create(Product(**product.dict()))
    
    
    

@router.get('/', response_model=List[ShowproductSchema])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, product: ProductSchema,repository: ProductRepository = Depends()):
    repository.update(id,product.dict())


@router.get('/{id}, response_model=ShowProductSchema')
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)