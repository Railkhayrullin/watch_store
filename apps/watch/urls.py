from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('watch/<slug:slug>', views.WatchDetailView.as_view(), name='watch'),
    # path("", views.FoodsView.as_view(), name="home"),
]
