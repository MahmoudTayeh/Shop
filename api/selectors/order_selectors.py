from api.models import Order

def order_list(filters=None):
    qs = Order.objects.select_related("user").prefetch_related("items__product").all()
    
    if filters:
        if "id" in filters:
            qs = qs.filter(id=filters["id"])
        if "user" in filters:
            qs = qs.filter(user__email=filters["user"])

    return qs