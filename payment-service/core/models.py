from django.db import models

class Payment(models.Model):
    order_id = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
