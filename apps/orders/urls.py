from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
]
