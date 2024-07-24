from django.forms import ModelForm
from django import forms
from shop import models as ShopModels

class BusinessForm(ModelForm):
    class Meta:
        model = ShopModels.Business
        fields = ("name", "description", "image",)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = ShopModels.Product
        fields = ("name", "description", "stock", "category", "price", "business")
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['business'].queryset = ShopModels.Business.objects.filter(owner=user)
