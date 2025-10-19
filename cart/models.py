from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Modelos del carrito
class Cart(models.Model):
    # Si el usuario esta logueado, se guarda aqui
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Para usuarios anonimos, usamos un session_key unico
    session_key = models.CharField(max_length=40, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update_at']

    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        return f"Anonumous Cart ({self.session_key})"
    
    # Metodo para calcular el total del carrito
    def get_total(self):
        total = sum(item.get_subtotal() for item in self.items.all())
        return total

    # metodo para contar items en el carrito
    def get_items_count(self):
        return sum(item.quantity for item in self.items.all())

# Modelo de Items del carrito
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # Guardamos el precio al momento de agregarlo (por si cambia despues)
    price_at_addition = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # un producto solo puede estar una vez en el mismo carrito
        unique_together = ('cart', 'product')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    # Calcular el subtotal de este item (precio x cantidad)
    def get_subtotal(self):
        return self.price_at_addition * self.quantity
    
    def save(self, *args, **kwargs):
        # auto-asiganr el precio actual del producto si no se especifica
        if not self.price_at_addition:
            self.price_at_addition = self.product.get_price()
        super().save(*args, **kwargs)