# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from e_products.models import ShoppingCart, Product, PurchaseItem
from e_products.serializers.purchase_item_serializer import PurchaseSerializer


class Checkout(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        shopping_cart = ShoppingCart.objects.get(user=user)

        # Calculate the total item amount and set it in the serializer
        total_item_amount = sum(
            cart_item.product.price * cart_item.quantity for cart_item in shopping_cart.products.all())
        serializer.validated_data['total_amount'] = total_item_amount

        # Create a new Purchase instance
        purchase = serializer.save(user=user)

        # Decrease stock_status and create PurchaseItem instances
        for cart_item in shopping_cart.products.all():
            product = cart_item.product
            product.stock_status -= cart_item.quantity
            product.save()

            # Calculate the item amount for each product
            item_amount = product.price * cart_item.quantity
            PurchaseItem.objects.create(purchase=purchase, product=product, quantity=cart_item.quantity,
                                        item_amount=item_amount)

        # Clear the shopping cart after successful purchase
        shopping_cart.products.clear()

    def create(self, request, *args, **kwargs):
        # Override the create method to include the total item amount in the response
        response = super().create(request, *args, **kwargs)
        purchase_serializer = self.get_serializer(response.data)
        response.data['total_item_amount'] = purchase_serializer.instance.total_amount
        return response
