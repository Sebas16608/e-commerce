from django.db import models
from django.utils.text import slugify

# Modelo Categoria
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        # Auto-generar slug si no existe
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
# Modelo Producto
class Product(models.Model):
    # Tipos de Productos
    PRODUCTS_TYPE_CHOICES = [
        ('physical', 'Producto Físico'),
        ('service', 'Servicio de Impresión'),
    ]

    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    # Relacion con categoria
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="producto")

    # Tipo del producto
    product_type = models.CharField(max_length=20, choices=PRODUCTS_TYPE_CHOICES, default='physical')

    # Precios
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
    # Precios con descuento
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Inventario
    stock = models.IntegerField(default=0)

    # Servicios, "Disponibilidad"
    is_avaible = models.BooleanField(default=True)

    # Especificaciones tecnicas
    material = models.CharField(max_length=100, blank=True)
    dimensions = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    print_time = models.CharField(max_length=100, blank=True)

    # SEO y metadatos
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    # Saber precio actual o con o sin descuento
    def get_price(self):
        if self.sale_price:
            return self.sale_price
        return self.price
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', 'order']

    def __str__(self):
        return f"Image for {self.product.name}"
