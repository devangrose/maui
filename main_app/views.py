from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index (request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

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
    if request.method == 'POST':
        # if user has a cart
        order = Order(
                product = Product.objects.get(pk=request.POST['product']),
                quantity = request.POST['quantity'],
                user_id = request.user
                )
        order.save()
        return redirect('cart')

    if request.method == 'GET':
        cart = Order.objects.all().filter(user_id = request.user.id)
        return render(request,'cart.html', {'cart':cart})
    return HttpResponse('Error');

def order_delete(request, order_id):
    Order.objects.get(pk=order_id).delete()
    return redirect('cart')

def checkout (request):
    return HttpResponse('Error');
