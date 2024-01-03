from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length = 20)
    product_category = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_expiry_date = models.DateField()
    product_manufacturing_date = models.DateField()
    product_HSN_no = models.IntegerField()
    product_quantity = models.IntegerField()

    class Meta:
        ordering = ['product_category']