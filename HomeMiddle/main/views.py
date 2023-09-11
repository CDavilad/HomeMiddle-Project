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