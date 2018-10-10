from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_show, name='product_show'),
    path('prodcut/new', views.product_new, name='product_new'),
    path('cart', views.cart, name='cart'),
    path('order/<int:order_id>/delete', views.order_delete, name='order_delete'),
    path('order/<int:order_id>/edit', views.order_edit, name='order_edit'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/coupon', views.coupon_code, name='coupon'),
    path('shirts', views.shirts, name='shirts'),
    path('pants', views.pants, name='pants'),
    path('order_history', views.order_history, name='order_history')
]
