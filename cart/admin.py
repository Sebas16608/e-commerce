from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemInLine(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('price_at_addition', 'added_at')
    fields = ('product', 'quantity', 'price_at_addition', 'added_at')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'get_items_count', 'get_total', 'update_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'session_key')
    readonly_fields = ('created_at', 'updated_at', 'get_total', 'get_items', 'update_at')

    inlines = [CartItemInLine]

    def get_items_count(self, obj):
        return obj.get_items_count()
    
    def get_total(self, obj):
        return f"Q{obj.get_total():.2f}"
    get_total.short_description = 'Total'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_at_addition', 'get_subtotal', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('product__name', 'cart__user__username')
    readonly_fields = ('price_at_addition', 'added_at', 'updated_at')
    
    def get_subtotal(self, obj):
        return f"Q{obj.get_subtotal():.2f}"
    get_subtotal.short_description = 'Subtotal'
    