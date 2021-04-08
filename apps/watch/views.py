from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, 'watch/index.html')


def about(request):
    return render(request, 'watch/about.html')


def shop(request):
    return render(request, 'watch/shop.html')
