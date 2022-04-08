from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.serializers import UserSerializer

from cart.models import *


class CartItemSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('user', 'product', 'cart', 'quantity', 'order')


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cart_products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'products', 'cart_products')


class OrderSerializer(serializers.ModelSerializer):
    cart_products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "email",
            "address",
            "descriptions",
            'cart_products',
            'status',
            "price",
        )
        read_only_fields = [
            "price",
            'cart_products'
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        cart = Cart.objects.filter(user=user.id).first()
        cart_products = cart.cart_products.all()

        if cart_products.first() == None:
            raise ValidationError(
                detail="your cart is empty, fill it and try again")

        instance = self.Meta.model._default_manager.create(
            price=cart.total_price,
            user=user,
            **validated_data
        )
        instance.cart_products.set(cart_products)

        cart.cart_products.set(CartItem.objects.none())
        return instance
