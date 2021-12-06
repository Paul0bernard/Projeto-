from fastapi import APIRouter, status , Depends
from app.models.models import Category
from .shchemas import SupplierSchema, ShowSupplierSchema 
from typing import List
from app.api.repositories.supplier_repository import SupplierRepository

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def creat(supllier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.create(Category(**supllier.dict()))     

@router.get('/', response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, product: SupplierSchema,repository: SupplierRepository = Depends()):
    repository.update(id,product.dict())


@router.get('/{id}, response_model=ShowSupplierSchema')
def show(id: int, repository: SupplierSchema = Depends()):
    return repository.get_by_id(id)
