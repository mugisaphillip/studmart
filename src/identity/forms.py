from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from identity import models as IdentityModels

class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = IdentityModels.User
        fields = ("username",)

class ProfileForm(ModelForm):
    class Meta:
        model = IdentityModels.User
        fields = ("email","surname","first_name","tel_number","isdelivery","account_type","institution","image",)


class AdminSignInForm(AuthenticationForm):
    class Meta:
        model = IdentityModels.User
        fields = ("username",)