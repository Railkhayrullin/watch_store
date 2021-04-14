from django import template

from apps.watch.views import get_current_order

register = template.Library()


@register.inclusion_tag('watch/inc/cart_popup.html')
def cart_popup(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    return context
