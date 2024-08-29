from django.db import models

class Product(models.Model):
    name = name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - Price: R${self.price}'
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - Stock: {self.stock}'