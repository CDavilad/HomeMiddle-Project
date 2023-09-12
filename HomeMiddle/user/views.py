from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from .models import *


# Create your views here.

class UserConfig(View):
    template_name='settings.html'

    def get(self, request):
        profile = Profile.objects.get(pk=request.user.id)
        form1 = UserForm()
        profileData = {"address": profile.address, "creditcard": profile.creditcard}
        form2 = ProfileForm(profileData)
        viewData = {}
        viewData["title"] = "User settings"
        viewData["user_form"] = form1
        viewData["profile_form"] = form2

        return render(request, self.template_name, viewData)
    
    def post(self, request):
        profile = Profile.objects.get(pk=request.user.id)
        if "first_name" in request.POST and "last_name" in request.POST and "email" in request.POST:
            print("Hola")
            profile.user.first_name = request.POST["first_name"]
            profile.user.last_name = request.POST["last_name"]
            profile.user.email = request.POST["email"]
            profile.user.save()
            return redirect('settings')
        elif "address" in request.POST and "creditcard" in request.POST:
            profile.address = request.POST["address"]
            if request.POST["creditcard"] =="":
                profile.creditcard = None
            else:
                profile.creditcard = request.POST["creditcard"]
            profile.save()
            return redirect('settings')
        else:
            viewData = {}
            viewData["title"] = "User settings"
            viewData["user_form"] = form1
            viewData["profile_form"] = form2

            return render(request, self.template_name, viewData)



    