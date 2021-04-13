from django.db import models

from apps.client_profile.models import Profile
from apps.watch.models import Product


class Order(models.Model):
    date = models.DateTimeField('datetime', auto_now_add=True)
    client_profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.CASCADE)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
    count = models.SmallIntegerField('count', default=1)
    price = models.FloatField('price', default=0)
