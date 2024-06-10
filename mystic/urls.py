# urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('sproduct/', views.sproduct, name='sproduct'),
]
