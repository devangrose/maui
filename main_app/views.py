from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index (request):
    products = Product.objects.all()
    print(products)
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
                description = form.cleaned_data['description']
                )
            product.save()
            return HttpResponse(product)
    return HttpResponse('Error');

def cart (request):
    if request.method == 'POST':
        # if user has a cart
        try: 
            cart =  Cart.objects.get(user_id = user.id)
            order = Order(
                    product = request.POST['product'],
                    quantity = int(request.POST['amount']),
                    user_id = user.id
                    )
            cart.orders.append(order)
            cart.save()
        # no cart, make new one
        except:
            cart = Cart(
                    user_id = user.id
                    )
            order = Order(
                    product = request.POST['product'],
                    quantity = int(request.POST['amount']),
                    user_id = user.id
                    )
            cart.orders.append(order)
            cart.save()
        return HttpResponse(cart)
    return HttpResponse('Error');

def checkout (request):
    return HttpResponse('Error');
