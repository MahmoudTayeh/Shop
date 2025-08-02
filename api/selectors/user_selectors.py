from account.models import CustomUser
from django.shortcuts import get_object_or_404
def customUser_list(filters=None):
    qs = CustomUser.objects.all()
    if filters:
        if 'username' in filters:
            qs = qs.filter(name__icontains=filters['username'])
        if 'email' in filters:
            qs = qs.filter(email__icontains=filters['email'])
    return qs

def customUser_get(pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        return user
    except CustomUser.DoesNotExist:
        return None