from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import logout, login
from django.contrib import messages
from identity import forms as IdentityForms
from identity import models as IdentityModels

class LoginView(View):
    template_name = "identity/login.html"
    context_data = {}

    def get(self, request):
        form = IdentityForms.AdminSignInForm()
        self.context_data["form"] = form

        return render(request, template_name=self.template_name, context=self.context_data)
    
    def post(self, request):
        form = IdentityForms.AdminSignInForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy("shop:home"))

        self.context_data["form"] = form
        messages.add_message(request, messages.ERROR, "Invalid username or password.")
        return render(request, template_name=self.template_name, context=self.context_data)
    
class SignUpView(View):
    template_name = "identity/signup.html"
    context_data={}

    def get(self, request):
        form = IdentityForms.AdminSignUpForm()
        self.context_data["form"] = form
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        form = IdentityForms.AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("identity:login"))
    
        self.context_data["form"] = form
        messages.add_message(request, messages.ERROR, "Invalid inputs.")
        return render(request, template_name=self.template_name, context=self.context_data)


def LogoutView(request):
    logout(request)
    return redirect(reverse_lazy("identity:login"))

def AccountTypeToggleView(request):
    # user must be logged in
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("identity:login"))
    
    user = IdentityModels.User.objects.filter(pk=request.user.pk)
    if not user:
        logout(request)
        return redirect(reverse_lazy("identity:login"))
    
    user = user.first()

    if user.account_type == "BUYER":
        user.account_type = "SELLER"
    else:
        user.account_type = "BUYER"

    user.save()
    return redirect(reverse_lazy("shop:home"))