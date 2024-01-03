from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    product_expiry_date = serializers.DateField(format="%Y-%m-%d")
    product_manufacturing_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Product
        fields = '__all__'
