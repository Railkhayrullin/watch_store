from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import NewsCategory, News, AboutItem, About, Contact


@admin.register(NewsCategory)
class NewsCategory(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'get_image', 'publish']
    list_editable = ['publish', ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="80">')
    get_image.short_description = 'image'


class AboutItemInline(admin.TabularInline):
    model = AboutItem
    extra = 0


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AboutItemInline, ]

    def has_add_permission(self, request):
        """The function does not allow adding objects larger than 'max_objects' """
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['title', 'slug',  'contact_phone', 'email']
    prepopulated_fields = {'slug': ('title',)}

    def has_add_permission(self, request):
        """The function does not allow adding objects larger than 'max_objects' """
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)
