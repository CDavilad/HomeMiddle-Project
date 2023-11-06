from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Furniture(models.Model):
    name = models.CharField(_('name'),max_length=255)
    type = models.CharField(_('type'),max_length=255)
    maker = models.CharField(_('maker'),max_length=255)
    material = models.CharField(_('material'),max_length=255)
    description = models.CharField(_('description'),max_length=2048)
    price = models.DecimalField(_('price'),max_digits=10, decimal_places=2)
    associated_furnitures = models.ManyToManyField('self', _('associated_fornitures'),blank=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Agrega un campo para el usuario si es necesario
    items = models.ManyToManyField(Furniture)

    def __str__(self):
        return f"Shopping Cart for {self.user.username}" 
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Furniture')  # Suponiendo que tienes un modelo Furniture para representar los productos
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Puedes personalizar esto según tus necesidades

    def __str__(self):
        return f'Order #{self.pk} - {self.user.username}'

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Agrega un campo para el usuario si es necesario
    items = models.ManyToManyField(Furniture)

    def __str__(self):
        return f"Wish List for {self.user.username}" 

class Review(models.Model):
  content = models.CharField(_('content'),max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Furniture, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.text

