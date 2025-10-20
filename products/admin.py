from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.

# Inline para mostrar imagenes dentro del producto
class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'is_primary', 'order')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'is_active', 'created_at')
    list_filter = ('category','product_type', 'price', 'sale_price', 'stock', 'is_available', 'featured', 'created_at')
    search_fields = ('name', 'product_type', 'is_avaible', 'featured', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'is_available', 'featured')

    # Mostrar imagenes dentro de cada formulario del producto
    inlines = [ProductImageInLine]

    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'slug', 'description', 'category', 'product_type') 
        }),
        ('Especificaciones Técnicas', {
            'fields': ('price', 'sale_price', 'stock', 'is_available')
        }),
        ('SEO y Marketing', {
            'fields': ('featured', 'views'),
            'classes': ('collapse',)
        })
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary', 'order', 'created_at')
    list_filter = ('is_primary', 'created_at')
    list_editable = ('is_primary', 'order')