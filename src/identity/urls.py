from django.urls import path
from identity import views as IdentityViews

app_name = "identity"

urlpatterns = [
    path("login/", IdentityViews.LoginView.as_view(), name="login"),
    path("signup/", IdentityViews.SignUpView.as_view(), name="signup"),
    path("logout/", IdentityViews.LogoutView, name="logout")
]