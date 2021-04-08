from django.shortcuts import render
from apps.pages.models import About
from django.views.generic import ListView, DetailView
from apps.pages.models import About, Contact


def index(request):
    return render(request, 'watch/index.html')


def about(request):
    context = {}
    page = About.objects.get(slug='about')
    context['page'] = page
    return render(request, 'watch/about.html', context)


def contact(request):
    context = {}
    page = Contact.objects.get(slug='contact')
    context['page'] = page
    return render(request, 'watch/contact.html', context)


def shop(request):
    return render(request, 'watch/shop.html')

