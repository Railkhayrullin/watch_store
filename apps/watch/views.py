from django.shortcuts import render
from django.http import Http404

from django.views.generic import ListView, DetailView
from apps.watch.models import Product, Price
from apps.pages.models import About, Contact, News


def index(request):
    context = {}

    discount = Product.objects.filter(publish=True, with_discount=True)
    context['discount'] = discount
    new_arrival = Product.objects.filter(publish=True,).order_by('-pk')[:3]
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
# def shop(request):
#     return render(request, 'watch/shop.html')


class BlogListView(ListView):
    paginate_by = 3
    model = News
    template_name = 'watch/blog.html'


class WatchDetailView(DetailView):
    model = Product
    template_name = 'watch/product_detail.html'
