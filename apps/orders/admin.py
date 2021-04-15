from django.contrib import admin
from apps.orders.models import Order, OrderDetail


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0
    fields = ['product', 'count', 'price', 'get_total_order', 'get_discount_order']
    readonly_fields = ['get_total_order', 'get_discount_order']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'client_profile', 'get_total', 'id']
    inlines = [OrderDetailInline, ]
