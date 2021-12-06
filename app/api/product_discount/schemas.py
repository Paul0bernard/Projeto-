
from app.api.produtc.schemas import ShowproductSchema
from app.api.payment_methods.schemas import PaymentMethodSchema
from pydantic import BaseModel
from enum import Enum


class DiscountMode(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'


class ProductDiscountSchema(BaseModel):
    product_id: int
    value: float
    payment_method_id: int
    mode: DiscountMode


class ShowProductDiscountsSchema(ProductDiscountSchema):
    product: ShowproductSchema
    payment_method: PaymentMethodSchema

    class Config:
        orm_mode = True