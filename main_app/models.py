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
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField(default = 0)

    def update_price(self):
        self.price = int(self.product.price) * int(self.quantity)


    def __str__(self):
        return str(self.product) + ', ' + str(self.quantity)

class Cart(models.Model):
    orders = models.ManyToManyField(Order, related_name='CartOrders')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    closed = models.BooleanField(default = False)
    date = models.DateField(default=datetime.datetime.now)
    price = models.IntegerField(default = 0)
    session_id = models.CharField(max_length=100,default='none')
    coupon = models.FloatField(default = 1)
    coupon_code = models.CharField(max_length=100, null=True, default=None)
    discount_amount = models.IntegerField(default=0)
    final_price = models.IntegerField(default = 0)

    def update_price(self):
        total_sum = 0
        for order in self.orders.all():
            total_sum += order.price
        self.price = total_sum
        if self.coupon != 1.0:
            self.discount_amount = total_sum * self.coupon
        self.final_price = total_sum - self.discount_amount

    def __str__(self):
        return str(self.user_id)
