from django.contrib import admin

from e_products.models import Product, ShoppingCart, CartItem, Purchase, PurchaseItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'image', 'stock_status']


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'display_products']

    def display_products(self, obj):  # for M2M relationship
        return ', '.join([str(item) for item in obj.products.all()])

    display_products.short_description = 'Products'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'shopping_cart', 'product', 'quantity']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'purchase_products', 'shipping_address', 'payment_details', 'total_amount',
                    'created_at']

    def purchase_products(self, obj):  # for M2M relationship
        return ', '.join([str(item) for item in obj.products.all()])

    purchase_products.short_description = 'Products'


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'purchase', 'product', 'quantity']
