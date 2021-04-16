from django.contrib.sessions.models import Session
from django.db import models

from apps.client_profile.models import Profile
from apps.watch.models import Product


class Status(models.Model):
    title = models.CharField('status', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'


class Order(models.Model):
    date = models.DateTimeField('datetime', auto_now_add=True)
    client_profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.CASCADE, blank=True,
                                       null=True)
    session = models.ForeignKey(Session, related_name='session_orders', on_delete=models.SET_NULL, blank=True,
                                null=True)
    first_name = models.CharField('имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=255, blank=True, null=True)
    number = models.CharField('телефон', max_length=20, blank=True, null=True)
    email = models.EmailField('email', max_length=255, blank=True, null=True)
    district = models.CharField('область', max_length=255, blank=True, null=True)
    city = models.CharField('город', max_length=255, blank=True, null=True)
    address = models.CharField('адрес', max_length=255, blank=True, null=True)
    post_code = models.CharField('почтовый индекс', max_length=255, blank=True, null=True)
    comment = models.TextField('комментарии к заказу', max_length=1000, blank=True, null=True)
    status = models.ForeignKey(Status, related_name='status_orders', on_delete=models.CASCADE, blank=True, null=True)

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

    def get_discount_order(self):
        default_total = self.product.get_regular_price() * self.count
        discount_total_order = default_total - self.get_total_order()
        return discount_total_order

    get_discount_order.short_description = 'total discount'
