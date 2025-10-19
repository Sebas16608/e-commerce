from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid
# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", null=True, blank=True)

    # Datos del destinatario
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    # Direccion
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=300, blank=True)
    municipio = models.CharField(max_length=100, help_text="Municipio")
    departamento = models.CharField(max_length=100, help_text="Departamento")
    zona = models.CharField(max_length=20, help_text="Zona")
    city = models.CharField(max_length=100, default="Guatemala")

    # Referencias
    reference = models.TextField(help_text="Punto de referencia para encontrar la direccion (gasolinera, iglesia, institucion, parque, etc)")

    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f"{self.full_name} - zona {self.zona}, {self.municipio}, {self.departamento}"
    