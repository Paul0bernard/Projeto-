from fastapi import APIRouter, status , Depends
from app.models.models import Category
from .schemas import CategorySchema, ShowCategorySchema 
from typing import List
from app.api.repositories.category_repository import CategoryRepository

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def creat(category: CategorySchema, repository: CategoryRepository = Depends()):
    repository.create(Category(**category.dict()))
    
    

@router.get('/', response_model=List[ShowCategorySchema])
def index(repository: CategoryRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, product: CategorySchema,repository: CategoryRepository = Depends()):
    repository.update(id,product.dict())


@router.get('/{id}, response_model=ShowCategorySchema')
def show(id: int, repository: CategorySchema = Depends()):
    return repository.get_by_id(id)
