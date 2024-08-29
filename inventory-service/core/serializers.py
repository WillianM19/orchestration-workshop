from rest_framework import serializers
from .models import Inventory, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer() 

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'stock']