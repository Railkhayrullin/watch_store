from django.contrib import admin
from django.utils.safestring import mark_safe

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
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'country', 'brand', 'get_image', 'publish']
    list_editable = ['publish', ]
    inlines = [PriceInline, ]
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="75">')
    get_image.short_description = 'image'
