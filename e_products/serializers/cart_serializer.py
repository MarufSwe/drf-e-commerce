from django.contrib.auth.models import User
from rest_framework import serializers
from e_products.models import CartItem, ShoppingCart, Product


class UserSerializerForCartItem(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ProductSerializerForCartItem(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image')


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializerForCartItem(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'product')


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = UserSerializerForCartItem(read_only=True)
    products = CartItemSerializer(source='cartitem_set', many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ('id', 'user', 'products')
