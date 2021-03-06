from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime

# Create your views here.
def index (request):
    if not request.session.session_key:
        request.session.create()
    shirts = Product.objects.all().filter(product_type='shirt')[:3]
    pants = Product.objects.all().filter(product_type='pants')
    return render(request, 'home.html', {'shirts':shirts, 'pants':pants})

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
                )[0]
    else:
        current_cart = Cart.objects.get_or_create(
                user_id = request.user,
                closed = False
                )[0]
    if request.method == 'POST':
        order = Order(
                product = Product.objects.get(pk=request.POST['product']),
                quantity = request.POST['quantity'],
                )
        order.update_price()
        order.save()
        current_cart.orders.add(order)
        current_cart.update_price()
        current_cart.save()
        request.session['cart'] = len(current_cart.orders.all())
        request.session['message'] = "Successfully added to cart"
        return redirect(request.POST.get('next','index'))

    if request.method == 'GET':
        orders = current_cart.orders.all()
        current_cart.update_price()
        request.session['cart'] = len(current_cart.orders.all())
        current_cart.save()
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
                )[0]
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
    if not request.user.id:
        cart = Cart.objects.get_or_create(
                session_id = request.session.session_key,
                closed = False
                )[0]
    else:
        cart = Cart.objects.get_or_create(
                user_id = request.user,
                closed = False
                )[0]
    if request.method == 'GET':
        return render(request, 'checkout.html',{'orders':cart.orders.all(),'current':cart})
    else:
        cart.closed = True
        if request.user.id is not None:
            cart.user_id = request.user
            cart.save()
        else:
            cart.delete()
        request.session['cart'] = 0
        if request.user.is_authenticated:
            return redirect('order_history') 
        else: 
            return redirect('index')

def coupon_code(request):
    if not request.user.id:
        cart = Cart.objects.get_or_create(
                session_id = request.session.session_key,
                closed = False
                )[0]
    else:
        cart = Cart.objects.get_or_create(
                user_id = request.user,
                closed = False
                )[0]
    if request.POST['coupon'] == 'MAUI':
        cart.coupon = 0.3
        cart.coupon_code = "MAUI"
        cart.update_price()
        print(cart.price)
        cart.save()

    return redirect('checkout')
    
def order_history (request):
    carts = Cart.objects.all().filter(user_id = request.user.id, closed=True)
    return render(request, 'order_history.html', {'carts':carts})
