from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User



# Create your models here.
class Product(models.Model):
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_type=models.CharField(max_length=100, default="shirt")
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product) + ', ' + str(self.quantity)
class Cart(models.Model):
    orders = models.ManyToManyField(Order, related_name='CartOrders')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user_id)
