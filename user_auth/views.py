from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from main_app.models import *

# Main routes
# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        #try:
        user = User.objects.create_user(username=username, 
                        password=password,
                        first_name=firstname,
                        last_name=lastname)
        if user is not None:
            return login(request)
            

def login(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'todoapp/login.html')
    elif request.method == 'POST':
        try:
            session_cart = Cart.objects.get(
                    session_id = request.session.session_key,
                    closed = False
                    )
        except:
            session_cart = None
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if session_cart:
                session_cart.user_id = user
                session_cart.save()
            auth.login(request, user)
            return redirect('index')
        else:
            print('error') 
            return render(
                    request,
                    'todoapp/login.html',
                    {
                        'error':'There has been an error',
                    })

def logout(request):
    auth.logout(request)
    return redirect('index')
