from django import template
from apps.watch.models import Category

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.filter(publish=True)

