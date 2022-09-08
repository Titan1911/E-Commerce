from django.contrib import admin
from .models import *

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)

    class Meta:
        model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # readonly_fields = ('total_price', 'total_items')

    class Meta:
        model = Cart