from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /inventario/
    path('', views.index, name='index'),
]