from django.urls import path
from shop import views as ShopViews

app_name = "shop"

urlpatterns = [
    path('', ShopViews.HomeView.as_view(), name="home"),
    path("404", ShopViews.error_404_view, name='error-page'),
    
    path('institution/<str:slug>/', ShopViews.InstitutionDetails.as_view(), name="institution-details"),

    path('products/', ShopViews.ProductListView.as_view(), name="product-list"),
    path('product/<str:slug>/', ShopViews.ProductDetailView.as_view(), name="product-details"),
    path('product/<str:slug>/cart/add/', ShopViews.AddProductToCartView.as_view(), name="add-to-cart"),
    path('cart/', ShopViews.CartView.as_view(), name="cart"),

    path('businesses/', ShopViews.BusinessListView.as_view(), name="business-list"),
    path('business/<str:slug>/', ShopViews.BusinessDetailView.as_view(), name="business-details"),
]