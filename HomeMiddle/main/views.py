from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms
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

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["furnitures_in_sc"] = furnitures_in_sc

    return render(request, 'shopping_cart.html', viewData)

def remove_from_shopping_cart(request, furniture_id):
    user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=user).first()
    if shopping_cart:
        furniture = get_object_or_404(Furniture, id=furniture_id)
        shopping_cart.items.remove(furniture)

    return redirect('shopping_cart')
