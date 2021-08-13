from django.contrib import admin

from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'cart_items_count', 'date_created')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)