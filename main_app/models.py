from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Product(models.Model):
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user_id = models.IntegerField()
    quantity = models.IntegerField()
class Cart(models.Model):
    orders = models.ManyToManyField(Order, related_name='CartOrders')
    user_id = models.IntegerField()
