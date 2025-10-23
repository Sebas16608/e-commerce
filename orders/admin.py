from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem, OrderTracking

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'product_name', 'price', 'quantity', 'get_subtotal')
    fields = ('product', 'product_name', 'quantity', 'price', 'get_subtotal')
    
    def get_subtotal(self, obj):
        return f"Q{obj.get_subtotal():.2f}"
    get_subtotal.short_description = 'Subtotal'

class OrderTrackingInline(admin.TabularInline):
    model = OrderTracking
    extra = 1
    fields = ('status', 'message', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'payment_method', 'total', 'is_paid', 'created_at')
    list_filter = ('status', 'payment_method', 'is_paid', 'created_at')
    search_fields = ('order_number', 'user__username', 'user__email', 'guest_email')
    readonly_fields = ('order_number', 'created_at', 'updated_at', 'paid_at')
    list_editable = ('status', 'is_paid')
    
    inlines = [OrderItemInline, OrderTrackingInline]
    
    fieldsets = (
        ('Información de Orden', {
            'fields': ('order_number', 'user', 'guest_email', 'status', 'created_at', 'updated_at')
        }),
        ('Pago', {
            'fields': ('payment_method', 'is_paid', 'paid_at')
        }),
        ('Montos', {
            'fields': ('subtotal', 'shipping_cost', 'tax', 'total')
        }),
        ('Envío', {
            'fields': ('shipping_address',)
        }),
        ('Notas', {
            'fields': ('customer_notes', 'admin_notes'),
            'classes': ('collapse',)
        }),
    )
    
    def get_total(self, obj):
        return f"Q{obj.total:.2f}"
    get_total.short_description = 'Total'

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'zona', 'municipio', 'departamento', 'is_default')
    list_filter = ('departamento', 'municipio', 'is_default')
    search_fields = ('full_name', 'phone', 'email', 'municipio', 'departamento')
    list_editable = ('is_default',)

@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'message', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__order_number', 'message')