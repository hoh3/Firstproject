from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
    context = {
        'title':"Home",
        }
    return render(request,'home.html',context)

def custom_post(request):
    context = {
        'content': Custom.objects.all(),
    }
    return render(request,'custom_new.html', context)

@csrf_exempt
def suggestions(request):
    if request.method == 'GET':
        suggestions = Suggestion.objects.all()
        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]
        return JsonResponse(suggest)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")

def products(request):
    if request.method == "POST":
        form = product_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
            form = product_form()
            context = {
                'form':form
            }
    return render(request, 'menu.html', context)

def custom(request):
    if request.method == "POST":
        form = custom_form(request.POST, request.FILES)
        if form.is_valid():
            submit = form.cleaned_data['title']
            form.save(request)
    else:
        form = custom_form()
    context = {
        'title':"Custom",
        'form':form
    }
    return render(request,'custom.html', context)

def orders(request):
    if request.method == 'POST':
        form = order_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = order_form()
    context = {
        'title':'Order',
        'form':form
    }
    return render(request, 'order.html', context)
#Cart
def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)
    return redirect('/cart')

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def cart(request):
    if request.method == "POST":
        form = product_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
            form = product_form()
            context = {
                'form':form
            }
    return render(request,'cart.html',context)

#Register
def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = registration_form()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request, 'register.html', context)
