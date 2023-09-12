from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from decimal import Decimal
from .models import *
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'


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

    return render(request, 'buy_sc.html', {'order': order})


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