# serializers.py
from rest_framework import serializers

from e_products.models import PurchaseItem, Purchase
from e_products.serializers.product_serializer import ProductSerializer


class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PurchaseItem
        fields = ('product', 'quantity', 'item_amount')


class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True, read_only=True)
    total_item_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Purchase
        fields = (
        'id', 'user', 'items', 'shipping_address', 'payment_details', 'total_amount', 'created_at', 'total_item_amount')
