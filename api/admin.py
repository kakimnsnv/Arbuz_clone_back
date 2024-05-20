from django.contrib import admin
from .models import Product, Cart, CartItem, Collection

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'remark', 'tags', 'description', 'price', 'imageUrl', 'minAmount', 'amountType', 'isLiked']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'item_count']
    
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Item Count'
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount']
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_count']
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Product Count'