from django.contrib import admin
from apps.orders.models import Order, OrderDetail


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_profile', 'date']
    inlines = [OrderDetailInline, ]
