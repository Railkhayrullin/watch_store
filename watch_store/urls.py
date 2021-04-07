from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('watch.urls')),
    path('admin/', admin.site.urls),
]
