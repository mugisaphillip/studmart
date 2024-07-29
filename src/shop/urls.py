from django.urls import path
from shop import views as ShopViews

app_name = "shop"

urlpatterns = [
    path('', ShopViews.HomeView.as_view(), name="home"),
    path('landing/', ShopViews.LandingPageView.as_view(), name="landing"),
    path("404", ShopViews.error_404_view, name='error-page'),
    
    path('institution/<str:slug>/', ShopViews.InstitutionDetails.as_view(), name="institution-details"),

    path('products/', ShopViews.ProductListView.as_view(), name="product-list"),
    path('product/<str:slug>/', ShopViews.ProductDetailView.as_view(), name="product-details"),

    path('cart/', ShopViews.CartOrdersView.as_view(), name="cart"),
    path('cart/placeorder', ShopViews.CartToOrderView.as_view(), name="cart-to-order"),
    path('product/<str:slug>/cart/add/', ShopViews.AddProductToCartView.as_view(), name="add-to-cart"),
    path('product/<str:slug>/cart/delete/', ShopViews.DeleteProductToCartView.as_view(), name="remove-from-cart"),

    path('businesses/', ShopViews.BusinessListView.as_view(), name="business-list"),
    path('business/<str:slug>/', ShopViews.BusinessDetailView.as_view(), name="business-details"),

    path("seller/dashboard/", ShopViews.SellerDashboard.as_view(), name="seller-dashboard"),
    path("seller/dashboard/business", ShopViews.SellerDashboardBusiness.as_view(), name="seller-dashboard-businesses"),
    path("seller/dashboard/products", ShopViews.SellerDashboardProducts.as_view(), name="seller-dashboard-products"),
    path("seller/dashboard/profile", ShopViews.SellerDashboardProfile.as_view(), name="seller-dashboard-profile"),
    path("seller/order/<int:pk>", ShopViews.SellerDashboardOrderStatus.as_view(), name="seller-order-status"),
]