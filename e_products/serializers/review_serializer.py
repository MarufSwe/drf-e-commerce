from rest_framework import serializers

from e_products.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'rating', 'comment')
