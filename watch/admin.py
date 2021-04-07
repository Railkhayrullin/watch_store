from django.contrib import admin
from .models import Brand, CaseMaterial, Category, Country, PriceType, Product, Price


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CaseMaterial)
class CaseMaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PriceType)
class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_editable = ['publish', ]


class PriceInline(admin.TabularInline):
    model = Price
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'country', 'brand', 'publish']
    list_editable = ['publish', ]
    inlines = [PriceInline, ]
    prepopulated_fields = {'slug': ('title',)}
