# # products/views.py
# from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
#
# from e_products.models import CartItem, Product
# from e_products.serializers.cart_serializer import CartItemSerializer
#
#
# class AddToCartView(generics.CreateAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]
#
#     def create(self, request, *args, **kwargs):
#         product_id = self.kwargs.get('pk')
#         product = generics.get_object_or_404(Product, id=product_id)
#
#         # Create a CartItem for the user
#         cart_item_data = {'user': request.user.id, 'product': product.id, 'quantity': 1}
#         cart_item_serializer = CartItemSerializer(data=cart_item_data)
#         cart_item_serializer.is_valid(raise_exception=True)
#         cart_item_serializer.save()
#
#         headers = self.get_success_headers(cart_item_serializer.data)
#         return Response(cart_item_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]
#
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from e_products.models import ShoppingCart, CartItem, Product
from e_products.serializers.cart_serializer import ShoppingCartSerializer, CartItemSerializer


# Product list into Cart for user
class ShoppingCartDetail(generics.RetrieveUpdateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__id'  # Use the authenticated user's ID as the lookup field

    def get_object(self):
        user = self.request.user
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, user=user)
        self.check_object_permissions(self.request, obj)
        return obj


# Add Product to Cart
class CartItemCreate(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        shopping_cart, created = ShoppingCart.objects.get_or_create(user=user)

        product_data = self.request.data.get('products', [{}])[0]
        product_id = product_data.get('product')
        quantity = product_data.get('quantity', 1)  # Default to 1 if not provided

        product = get_object_or_404(Product, id=product_id)

        # Check if the product is already in the cart
        existing_cart_item = CartItem.objects.filter(shopping_cart=shopping_cart, product=product).first()

        if existing_cart_item:
            # If the product is already in the cart, update the quantity
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
            serializer.instance = existing_cart_item
        else:
            # If the product is not in the cart, create a new CartItem
            serializer.save(shopping_cart=shopping_cart, product=product, quantity=quantity)


# Remove Product from Cart
class CartItemDelete(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')  # Assuming the product_id is passed in the URL
        return get_object_or_404(CartItem, shopping_cart__user=user, product__id=product_id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Product removed from cart successfully"}, status=status.HTTP_204_NO_CONTENT)
