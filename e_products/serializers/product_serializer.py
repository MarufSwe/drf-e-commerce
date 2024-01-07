from rest_framework import serializers

from e_products.models import Product
from e_products.serializers.review_serializer import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'stock_status', 'reviews')
