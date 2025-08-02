from django.urls import path
from .views.user_views import UserListApi
from .views.product_views import ProductListApi,ProductUpdateApi

urlpatterns = [
    path('users/', UserListApi.as_view(), name='user-list'),
    path('products/', ProductListApi.as_view(), name='product_list'),
    path('products/<int:product_id>/',ProductUpdateApi.as_view(),name='product_update')
]
