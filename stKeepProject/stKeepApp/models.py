from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=150)

    def _str__(self):
        return {f"{self.name}, {self.supplier}"}

    