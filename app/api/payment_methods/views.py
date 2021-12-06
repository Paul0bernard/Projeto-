from fastapi import APIRouter, status , Depends
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema 
from typing import List
from app.api.repositories.payment_methods_repository import PaymentMethodsRepository

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def creat(payment_method:PaymentMethodSchema, repository: PaymentMethodSchema = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))
    
    

@router.get('/', response_model=List[ShowPaymentMethodSchema])
def index(repository: PaymentMethodsRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id: int, product:PaymentMethodSchema,repository: PaymentMethodSchema = Depends()):
    repository.update(id,product.dict())


@router.get('/{id}, response_model=ShowCategorySchema')
def show(id: int, repository: PaymentMethodSchema = Depends()):
    return repository.get_by_id(id)