from api.models import Product 
from api.selectors.product_selectors import product_get

def product_update(pk:int , data:dict):
    product = product_get(pk)
    for field,value in data.items():
        setattr(product,field,value)
    product.save()
    return product
def product_delete(pk):
    product = product_get(pk)
    if product : product.delete()
    return product