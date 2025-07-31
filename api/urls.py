from django.urls import path
from .views import UserListApi

urlpatterns = [
    path('users/', UserListApi.as_view(), name='user-list'),
]
