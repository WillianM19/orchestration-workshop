from django.db import models

class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    
    
