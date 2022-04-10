from django.urls import path, include
from rest_framework import routers

from cart.views import *

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart_products', CartItemViewSet, basename='cart_products')

urlpatterns = [
    path('cart/', include(router.urls))
]
