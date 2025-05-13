from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem

# Customize the Product display
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'stock', 'created_at']
    search_fields = ['name', 'category']
    list_filter = ['category']
    ordering = ['-created_at']

# CartItem display
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    search_fields = ['user__username', 'product__name']

# Order display
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_ordered', 'is_completed']
    list_filter = ['is_completed', 'date_ordered']
    search_fields = ['user__username']

# OrderItem display
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']
    search_fields = ['product__name', 'order__id']
