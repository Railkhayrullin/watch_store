from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from apps.watch.views import get_current_order
from .forms import OrderForm
from django.conf import settings

# Create your views here.
from .models import Status


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


def checkout(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order.status = Status.objects.get(slug='waiting')
            order.save()
            context['result'] = True

            html = render_to_string('email/email.html', {'order': order})
            if not settings.DEBUG:
                send_mail('Сообщение с сайта watch_store.com', html, settings.DEFAULT_FROM_EMAIL,
                          get_managers_emails(), html_message=html)
            else:
                print(html)

    context['form'] = OrderForm()
    return render(request, 'orders/checkout.html', context)


def get_managers_emails():
    emails = []
    users = settings.AUTH_USER_MODEL.objects.filter(groups__name='managers')
    for user in users:
        if user.email:
            emails.append(user.email)
    return emails
