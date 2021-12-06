from fastapi import Depends
from app.api.repositories.payment_methods_repository import PaymentMethodsRepository
from app.api.repositories.product_discount_repository import ProductDiscountRepository
from app.api.repositories.product_repository import ProductRepository

class ProductDiscountService: 
    def __init__ (self, payment_method_repository: PaymentMethodsRepository = Depends(), 
                      product_discount_repository: ProductDiscountRepository = Depends):
     self.payment_method_repository = payment_method_repository
     self.payment_method_repository = product_discount_repository 

    def create_discount(self, discount: ProductRepository):
        pass 