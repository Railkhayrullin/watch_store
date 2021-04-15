from django.contrib.sessions.models import Session
from django.db import models

from apps.client_profile.models import Profile
from apps.watch.models import Product


class Order(models.Model):
    date = models.DateTimeField('datetime', auto_now_add=True)
    client_profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.CASCADE, blank=True,
                                       null=True)
    session = models.ForeignKey(Session, related_name='session_orders', on_delete=models.SET_NULL, blank=True,
                                null=True)

    def __str__(self):
        return str(self.date)

    def get_total(self):
        total = 0
        for detail in self.details.all():
            total += detail.get_total_order()
        return total
    get_total.short_description = 'total'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
    count = models.SmallIntegerField('count', default=1)
    price = models.FloatField('price', default=0)

    def __str__(self):
        return self.product.title

    def get_total_order(self):
        return self.count * self.price
    get_total_order.short_description = 'total order'
