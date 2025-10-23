from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid

# Modelo de Dirección de Envío
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)
    
    # Datos del destinatario
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    # Dirección adaptada para Guatemala
    address_line1 = models.CharField(max_length=300, help_text="Dirección principal (calle, avenida, número)")
    address_line2 = models.CharField(max_length=300, blank=True, help_text="Información adicional (casa, edificio, apartamento)")
    zona = models.CharField(max_length=20, help_text="Zona")
    municipio = models.CharField(max_length=100, help_text="Municipio")
    departamento = models.CharField(max_length=100, help_text="Departamento")
    country = models.CharField(max_length=100, default='Guatemala')
    
    # Referencias (esto SÍ es importante en Guatemala)
    reference = models.TextField(help_text="Punto de referencia para encontrar la dirección (gasolinera, iglesia, centro comercial, etc.)")
    
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Shipping Addresses"
    
    def __str__(self):
        return f"{self.full_name} - Zona {self.zona}, {self.municipio}, {self.departamento}"


# Modelo de Orden
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('processing', 'En Proceso'),
        ('shipped', 'Enviada'),
        ('delivered', 'Entregada'),
        ('cancelled', 'Cancelada'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Efectivo contra entrega'),
        ('transfer', 'Transferencia bancaria'),
        ('card', 'Tarjeta de crédito/débito'),
    ]
    
    # ID único de orden (lo que ve el cliente)
    order_number = models.CharField(max_length=50, unique=True, editable=False)
    
    # Usuario (puede ser null para compras como invitado)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    
    # Información de contacto (por si compra sin cuenta)
    guest_email = models.EmailField(blank=True)
    
    # Dirección de envío
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    
    # Estado y método de pago
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    # Montos
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Notas
    customer_notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    
    # Estado de pago
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        # Generar número de orden único
        if not self.order_number:
            self.order_number = f"MAX3D-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Order {self.order_number}"
    
    # Método para obtener el email (de usuario o invitado)
    def get_email(self):
        if self.user:
            return self.user.email
        return self.guest_email


# Modelo de Items de la Orden
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    
    # Guardamos toda la info del producto por si se elimina después
    product_name = models.CharField(max_length=300)
    product_sku = models.CharField(max_length=100, blank=True)
    
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity}x {self.product_name}"
    
    # Calcular subtotal del item
    def get_subtotal(self):
        return self.price * self.quantity


# Modelo de Tracking (para seguimiento de envío)
class OrderTracking(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tracking_updates')
    status = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.order.order_number} - {self.status}"