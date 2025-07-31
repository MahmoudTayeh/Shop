from account.models import CustomUser

def customUser_list(filters=None):
    qs = CustomUser.objects.all()
    if filters:
        if 'name' in filters:
            qs = qs.filter(name__icontains=filters['name'])
        if 'email' in filters:
            qs = qs.filter(email__icontains=filters['email'])
    return qs