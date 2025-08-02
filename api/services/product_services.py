from api.models import Product 
from api.selectors.product_selectors import product_get

def product_update(product_id:int , data:dict):
    product = product_get(product_id)
    for field,value in data.items():
        setattr(product,field,value)
    product.save()
    return product
