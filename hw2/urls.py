from django.urls import path
from .views import last_orders, order_info, add_product

urlpatterns = [
    path('orders/<int:client_id>/', last_orders, name='last_orders'),
    path('products/<int:order_id>/', order_info, name='order_info'),
    path('add_product/', add_product, name='add_product'),
]