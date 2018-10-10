from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime



# Create your models here.
class Product(models.Model):
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_type=models.CharField(max_length=100, default="shirt")
    price=models.IntegerField(default=30)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def price(self):
        return product.price * quantity

    def __str__(self):
        return str(self.product) + ', ' + str(self.quantity)
class Cart(models.Model):
    orders = models.ManyToManyField(Order, related_name='CartOrders')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    closed = models.BooleanField(default = False)
    date = models.DateField(default=datetime.datetime.now)

    def price(self):
        total_sum = 0
        for order in orders:
            total_sum += order.price()
        return total_sum

    def __str__(self):
        return str(self.user_id)
