from django.db import models
from django.contrib.auth.models import User

class Furniture(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    associated_furnitures = models.ManyToManyField('self', blank=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Agrega un campo para el usuario si es necesario
    items = models.ManyToManyField(Furniture)

    def __str__(self):
        return f"Shopping Cart for {self.user.username}" 