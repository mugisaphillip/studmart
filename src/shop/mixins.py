from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages

class SellerOnlyAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
    
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, "Login to access dashboard.")
            return redirect(reverse_lazy("identity:login"))
        
        if not request.user.account_type == "SELLER":
            messages.add_message(request, messages.ERROR, "Switch to seller mode to access dashboard.")
            return redirect(reverse_lazy("shop:home"))
        
        
        return super().dispatch(request, *args, **kwargs)