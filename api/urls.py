from django.urls import path
from .views.user_views import UserListApi,UserDeleteApi
from .views.product_views import ProductListApi,ProductDeleteApi,ProductUpdateApi,ProductCreateApi
from .views.order_views import OrderListApi
urlpatterns = [
    path('users/', UserListApi.as_view(), name='user-list'),
    path('users/<int:pk>/',UserDeleteApi.as_view(),name='user_delete'),
    path('products/list/', ProductListApi.as_view(), name='product_list'),
    path('products/<int:pk>/update/',ProductUpdateApi.as_view(),name='product_update'),
    path('products/<int:pk>/delete/',ProductDeleteApi.as_view(),name='product_delete'),
    path('products/creat/',ProductCreateApi.as_view(), name= 'product_create'),
    path('orders/list/', OrderListApi.as_view(),name='order_list'),
    
]
