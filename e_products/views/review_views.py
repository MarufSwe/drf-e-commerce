from rest_framework import generics

from e_products.models import Review
from e_products.serializers.review_serializer import ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
