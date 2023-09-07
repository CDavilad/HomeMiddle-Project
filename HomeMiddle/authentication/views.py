from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthenticateForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.views import View
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

class SignUpView(View):
    template_name= "signupaccount.html"

    def get(self, request):
        form = RegisterForm()
        viewData = {}
        viewData["title"] = "Create account"
        viewData["form"] = form

        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home')
        else:
            viewData = {}
            viewData["title"] = "Create account"
            viewData["form"] = form

            return render(request, self.template_name, viewData)

class LogInView(View):
    template_name= "loginaccount.html"

    def get(self, request):
        form = AuthenticateForm()
        viewData = {}
        viewData["title"] = "Log In account"
        viewData["form"] = form

        return render(request, self.template_name, viewData)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        if user is not None:
                login(request,user)
                return redirect('home')
        else:
            form = AuthenticateForm()
            viewData = {}
            viewData["title"] = "Log In account"
            viewData["form"] = form
            viewData["warning"] = "Wrong username or password"

            return render(request, self.template_name, viewData)
        

#@login_required       
def logoutaccount(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect("home")
