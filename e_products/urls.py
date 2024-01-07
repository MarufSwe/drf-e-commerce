from django.urls import path
from .views.product_views import ProductList, ProductDetail
from .views.product_cart_views import ShoppingCartDetail, CartItemCreate, CartItemDelete
from .views.purchase_checkout_views import Checkout
from .views.review_views import ReviewCreate, ReviewDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('reviews/', ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('cart/', ShoppingCartDetail.as_view(), name='shopping-cart'),
    path('cart/add/', CartItemCreate.as_view(), name='add-to-cart'),
    path('cart/remove/<int:product_id>/', CartItemDelete.as_view(), name='cartitem-delete'),

    path('checkout/', Checkout.as_view(), name='checkout'),

]
