from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cart.models import Cart, CartItem, Order


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'cart', 'quantity',
                  'order', 'final_price', 'price', 'title')
        read_olny_fields = ('price', 'final_price', "title")

    def create(self, validated_data):
        cart = Cart.objects.filter(
            user=self.context['request'].user.id).first()
        product = validated_data['product']
        if not product.available:
            raise ValidationError(detail='Нет в наличии')

        CartItem = self.Meta.model
        cart_product = CartItem.objects.filter(
            product=product, cart=cart).first()

        if cart_product:
            cart_product.quanity += validated_data.get('quanity')
            cart_product.save()
            return cart_product
        else:
            instance = CartItem._default_manager.create(
                cart=cart, **validated_data)
            return instance


class CartSerializer(serializers.ModelSerializer):
    cart_products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'total_price', 'cart_products')


class OrderSerializer(serializers.ModelSerializer):
    cart_products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'number', 'email',
                  'address', 'descriptions', 'price', 'cart_products')
        read_only_fields = ('price', 'cart_products')

    def create(self, validated_data):
        user = self.context['request'].user
        cart = Cart.objects.filter(user=user.id).first()
        cart_products = cart.cart_products.all()

        if cart_products.first() == None:
            raise ValidationError(detail='Ваша корзина пуста.')

        instance = self.Meta.model._default_manager.create(
            price=cart.total_price,
            user=user,
            **validated_data
        )
        instance.cart_products.set(cart_products)

        cart.cart_products.set(CartItem.objects.none())
        return instance
