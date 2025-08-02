from django.shortcuts import get_object_or_404
from api.models import Product 
def product_list(filters=None):
    qs = Product.objects.all()
    if filters:
        if 'name' in filters:
            qs = qs.filter(name__icontains=filters['name'])
        if 'price' in filters:
            qs = qs.filter(price__icontains=filters['price'])
    return qs

def product_get(pk):
    try:
        product = Product.objects.get(pk=pk)
        return product
    except Product.DoesNotExist:
        return None
