from django.shortcuts import render, redirect
from apps.watch.views import get_current_order


# Create your views here.
def cart(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    return render(request, 'orders/cart.html', context)


def delete_product(request, pk):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    if order.details.filter(pk=pk).exists():
        order.details.filter(pk=pk).delete()
    return redirect('cart')


def delete_cart(request):
    context = {}
    order = get_current_order(request)
    order.details.all().delete()
    return redirect('cart')
