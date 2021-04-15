from django.shortcuts import render
from apps.watch.views import get_current_order


# Create your views here.
def cart(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    return render(request, 'orders/cart.html', context)
