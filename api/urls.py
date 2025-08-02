from django.urls import path
from .views.user_views import UserListApi,UserDeleteApi
from .views.product_views import ProductListApi,ProductUpdateOrDeleteApi

urlpatterns = [
    path('users/', UserListApi.as_view(), name='user-list'),
    path('users/<int:pk>/',UserDeleteApi.as_view(),name='user_delete'),
    path('products/', ProductListApi.as_view(), name='product_list'),
    path('products/<int:pk>/',ProductUpdateOrDeleteApi.as_view(),name='product_update'),
    path('products/<int:pk>/',ProductUpdateOrDeleteApi.as_view(),name='product_delete'),
]
