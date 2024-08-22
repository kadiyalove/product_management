from django.db import models
from django.db import transaction
from django.db.models import F, Sum

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sales', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            # Reduce the inventory count
            self.product.inventory_count = F('inventory_count') - self.quantity
            self.product.save(update_fields=['inventory_count'])

    def __str__(self):
        return f"{self.quantity} of {self.product.name} sold on {self.sale_date}"