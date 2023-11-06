from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from decimal import Decimal
from .models import *
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import serializers 
import requests
import json
from django.http import FileResponse, HttpResponseNotFound,  HttpResponse
from .invertion import PDFPaymentProvider
import os
from django.core.files.storage import FileSystemStorage

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
 
    def get(self, request):
        url='http://api.weatherapi.com/v1/current.json?key=2f788c18a09248fda87224843230511&q=Medellin&aqi=no'
        response = requests.get(url)
        viewData = {}
        viewData["weather"] = response.json()
        return render(request, self.template_name, viewData)



class FurnitureShowView(View):
    template_name = 'show_furniture.html'

    def get(self, request, id):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["furniture"] = get_object_or_404(Furniture,pk=id)
        
        return render(request, self.template_name, viewData)

class FurnitureIndexView(TemplateView):
    template_name = 'furniture_index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["furnitures"] = Furniture.objects.all()

        return render(request, self.template_name, viewData)
    
class ReviewsPage(View):
    template_name = 'reviews.html'

    def get(self, request, id):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["furniture"] = get_object_or_404(Furniture,pk=id)
        
        return render(request, self.template_name, viewData)
    
class ShoppingCartPage(TemplateView):
    template_name = 'shopping_cart.html'

class AddedToShoppingCart(TemplateView):
    template_name = 'added_to_sc.html'

def add_to_shopping_cart(request, furniture_id):
    user = request.user
    furniture = get_object_or_404(Furniture, id=furniture_id)
    shopping_cart, created = ShoppingCart.objects.get_or_create(user=user)
    shopping_cart.items.add(furniture)
    if created:
        return redirect('added_to_sc')
    else:
        return redirect('added_to_sc')

    
def show_shopping_cart(request):
    user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=user).first()
    furnitures_in_sc = []
    if shopping_cart:
        furnitures_in_sc = shopping_cart.items.all()
    total = sum(furniture.price for furniture in furnitures_in_sc)

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["furnitures_in_sc"] = furnitures_in_sc
    viewData["total"] = total

    return render(request, 'shopping_cart.html', viewData)

def remove_from_shopping_cart(request, furniture_id):
    user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=user).first()
    if shopping_cart:
        furniture = get_object_or_404(Furniture, id=furniture_id)
        shopping_cart.items.remove(furniture)

    return redirect('shopping_cart')




def buy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    shopping_cart = ShoppingCart.objects.get(user=request.user)
    total_price = Decimal(0)
    for item in shopping_cart.items.all():
        total_price += item.price 
    order = Order.objects.create(user=request.user, total_price=total_price)
    for item in shopping_cart.items.all():
        order.items.add(item)
    shopping_cart.items.clear()
    payment_provider = PDFPaymentProvider()
    name=request.user.first_name + " " + request.user.last_name
    pdf_file = payment_provider.generate_payment_pdf(name, total_price, order)

    return render(request, 'buy_sc.html', {'order': order, 'pdf_file': pdf_file})


class WishListPage(TemplateView):
    template_name = 'wish_list.html'

class AddedToWishList(TemplateView):
    template_name = 'added_to_wl.html'

def add_to_wish_list(request, furniture_id):
    user = request.user
    furniture = get_object_or_404(Furniture, id=furniture_id)
    wish_list, created = WishList.objects.get_or_create(user=user)
    wish_list.items.add(furniture)
    if created:
        return redirect('added_to_wl')
    else:
        return redirect('added_to_wl')

def show_wish_list(request):
    user = request.user
    wish_list = WishList.objects.filter(user=user).first()
    furnitures_in_wl = []
    if wish_list:
        furnitures_in_wl = wish_list.items.all()

    viewData = {}
    viewData["title"] = "Wish List"
    viewData["subtitle"] =  "Wish List"
    viewData["furnitures_in_wl"] = furnitures_in_wl

    return render(request, 'wish_list.html', viewData)

def remove_from_wish_list(request, furniture_id):
    user = request.user
    wishList = WishList.objects.filter(user=user).first()
    if WishList:
        furniture = get_object_or_404(Furniture, id=furniture_id)
        wishList.items.remove(furniture)

    return redirect('wish_list')

@login_required    
def createReview(request, product_id):
    product = get_object_or_404(Furniture,pk=product_id)
    if request.method == 'GET':
        return render(request, 'reviews.html', {'form':ReviewForm(), 'product':product})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.created_by = request.user
            newReview.product = product
            newReview.save()
            return redirect('furniture_index')
        
        except ValueError:
          return render(request,'reviews.html', {'form':ReviewForm(), 'error':'bad data passed in'})

def get_service_team(request):
    url='http://127.0.0.1:8000/api/furniture'
    response = requests.get(url)

    if response.status_code == 200:
        return HttpResponse(response.json())





    