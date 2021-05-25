from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('contact/', views.contact, name='contact'),
    path('watch/<slug:slug>/', views.product_detail, name='watch'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
