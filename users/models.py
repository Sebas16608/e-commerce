from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo del perfil del usuario
class UserProfile(models.Model):
    # relacion uno a uno con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Informacion adicional
    phone = models.CharField(max_length=20)

    # Avatar o foto
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Preferencias
    newsletter_subscription = models.BooleanField(default=False)

    # Metadatos
    bio = models.TextField(blank=True, max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
# signal para crear automaticamente el perfil cuando se crea un usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Cuando se crea un nuevo usuario automaticamente se crea su perfil
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    cuando se guarda un usuario, tambien se guarda su perfil
    """
    instance.profile.save()