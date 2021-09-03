
from Proyecto1.views import saludo
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
