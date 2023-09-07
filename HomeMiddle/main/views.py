from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View
from django import forms
from .models import *
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'