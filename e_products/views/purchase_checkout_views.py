# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from e_products.models import ShoppingCart, Product, PurchaseItem
from e_products.serializers.purchase_item_serializer import PurchaseSerializer


class Checkout(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        shopping_cart = ShoppingCart.objects.get(user=user)
        purchase = serializer.save(user=user, total_amount=shopping_cart.calculate_total())

        # Decrease stock_status and create PurchaseItem instances
        for cart_item in shopping_cart.cart_items.all():
            product = cart_item.product
            product.stock_status -= cart_item.quantity
            product.save()
            PurchaseItem.objects.create(purchase=purchase, product=product, quantity=cart_item.quantity)

        # Clear the shopping cart after successful purchase
        shopping_cart.cart_items.all().delete()
