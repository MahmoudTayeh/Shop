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

def product_get(product_id):
    product = get_object_or_404(Product, id=product_id)
    return product
