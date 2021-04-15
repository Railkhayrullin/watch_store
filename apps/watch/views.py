from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from apps.watch.models import Product
from apps.pages.models import About, Contact, News
from apps.watch.forms import ProductForm
from apps.orders.models import Order, OrderDetail


def index(request):
    context = {}

    discount = Product.objects.filter(publish=True, with_discount=True)
    context['discount'] = discount
    new_arrival = Product.objects.filter(publish=True, ).order_by('-pk')[:3]
    context['new_arrival'] = new_arrival
    return render(request, 'watch/index.html', context)


def about(request):
    context = {}
    if About.objects.filter(slug='about').exists():
        page = About.objects.get(slug='about')
    else:
        raise Http404('Страница "О НАС" не найдена')

    context['page'] = page
    return render(request, 'watch/about.html', context)


def contact(request):
    context = {}
    if Contact.objects.filter(slug='contact').exists():
        page = Contact.objects.get(slug='contact')
    else:
        raise Http404('Страница "КОНТАКТЫ" не найдена')

    context['page'] = page
    return render(request, 'watch/contact.html', context)


class ShopListView(ListView):
    model = Product
    queryset = Product.objects.filter(publish=True)
    template_name = 'watch/shop.html'


class BlogListView(ListView):
    paginate_by = 3
    model = News
    template_name = 'watch/blog.html'


def product_detail(request, slug):
    context = {}

    if Product.objects.filter(slug=slug).exists():
        product = Product.objects.get(slug=slug)
        context['product'] = product
    else:
        raise Http404('Страница не найдена')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            order = get_current_order(request)
            count = form.cleaned_data['count']

            if order.details.filter(product=product).exists():
                # calc exists order_details
                order_details = order.details.filter(product=product).first()
                order_details.count += count
                order_details.save()
            else:
                # create new order_details
                order_details = OrderDetail()
                order_details.order = order
                order_details.count = count
                order_details.product = product
                order_details.price = product.get_current_price()
                order_details.save()
        context['success'] = True
        context['form'] = ProductForm()

    else:

        context['form'] = ProductForm()
    return render(request, 'watch/product_detail.html', context)


def get_current_order(request):
    if Order.objects.filter(session__session_key=request.session.session_key):
        return Order.objects.filter(session__session_key=request.session.session_key).first()
    else:
        order = Order()
        if not request.session.session_key:
            request.session.save()
        session = Session.objects.get(session_key=request.session.session_key)
        order.session = session
        order.save()
        return order


class SearchResultsView(ListView):
    model = Product
    template_name = 'watch/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__contains=query) |
            Q(category__title__contains=query) |
            Q(case_material__title__contains=query) |
            Q(country__title__contains=query) |
            Q(brand__title__contains=query)
        )
        return object_list
