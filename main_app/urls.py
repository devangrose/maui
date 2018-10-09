from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int: product_id', views.product_show, name='product_show'),
    path('prodcut/new', views.product_new, name='product_new'),
    path('cart', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
]
