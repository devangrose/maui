from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime

# Create your views here.
def index (request):
    if not request.session.session_key:
        request.session.create()
    print(request.session.session_key)
    print(request.user.id, 'user')
    return render(request, 'home.html')

def product_show(request, product_id):
    return HttpResponse(request, 'test');

def product_new(request):
    if request.method == 'POST':
        form = request.POST
        if form.is_vaild():
            product = Product(
                image_url = form.cleaned_data['image'],
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                product_type = form.cleaned_data['type'],
                )
            product.save()
            return HttpResponse(product)
    return HttpResponse('Error');

def cart (request):
    if not request.user.id:
        current_cart = Cart.objects.get_or_create(
                session_id = request.session.session_key,
                closed = False
                )
    else:
        current_cart = Cart.objects.get_or_create(
                user_id = request.user,
                closed = False
                )[0]
    if request.method == 'POST':
        order = Order(
                product = Product.objects.get(pk=request.POST['product']),
                quantity = request.POST['quantity'],
                user_id = request.user
                )
        order.update_price()
        order.save()
        current_cart.orders.add(order)
        current_cart.update_price()
        current_cart.save()
        return redirect('cart')

    if request.method == 'GET':
        orders = current_cart.orders.all()
        return render(request,'cart.html', {'cart':orders, 'current':current_cart})
    return HttpResponse('Error');

def order_edit(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.quantity=request.POST['quantity']
    order.update_price()
    order.save()

    if not request.user.id:
        current_cart = Cart.objects.get_or_create(
                session_id = request.session.session_key,
                closed = False
                )
    else:
        current_cart = Cart.objects.get_or_create(
                user_id = request.user,
                closed = False
                )[0]
    current_cart.update_price()
    return redirect('cart')

def order_delete(request, order_id):
    Order.objects.get(pk=order_id).delete()
    return redirect('cart')

def shirts(request):
    products = Product.objects.all().filter(product_type='shirt')
    return render(request,'shirts.html', {'products':products})

def pants(request):
    products = Product.objects.all().filter(product_type='pants')
    return render(request,'pants.html', {'products':products})

def checkout (request):
    cart = Cart.objects.get(
            user_id = request.user,
            closed = False
            )
    if request.method == 'GET':
        return render(request, 'checkout.html',{'orders':cart.orders.all(),'current':cart})
    else:
        cart.closed = True
        cart.save()
        return redirect('index') 
    
def order_history (request):
    carts = Cart.objects.all().filter(user_id = request.user.id, closed=True)
    return render(request, 'order_history.html', {'carts':carts})
