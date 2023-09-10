from django.db import models

class Furniture(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #associated_furnitures = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
