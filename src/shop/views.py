from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from shop import models as ShopModels
from identity import models as IdentityModels
from django.db.models import Q
from django.contrib import messages
import random, decimal


def error_404_view(request):
    return render(request, template_name="utils/404.html")

class InstitutionDetails(View):
    template_name = "shop/institution_details.html"
    context_data = {}

    def get(self, request, slug):
        institution = IdentityModels.Institution.objects.filter(slug=slug)
        if not institution:
            return redirect(reverse_lazy("shop:error-page"))

        institution = institution.first()
        self.context_data['institution'] = institution

        self.context_data["categories"] = ShopModels.Category.objects.filter(product_count__gte=1, business_count__gte=1)


        businesses = [businesss_link.business for businesss_link in institution.businessinstitution_set.all()]
        self.context_data["businesses"] = [
            {
                "business": business,
                'categories': [ category.category for category in ShopModels.BusinessCategory.objects.filter(business=business) ]
            } for business in (
                    lambda business: random.sample(business, len(business))
                )(list(businesses))
        ]

        products = []
        for business in businesses:
            products = [*products, *business.product_set.all()]

        self.context_data["products"] = [
            {
                "product": product,
                "images": ShopModels.ProductImage.objects.filter(product=product)[:2]
            } for product in (
                    lambda products: random.sample(products, len(products))
                )(list(products))[:15]
        ]

        return render(request, template_name=self.template_name, context=self.context_data)

class HomeView(View):
    template_name = "shop/index.html"
    context_data = {}

    def get(self, request):
        self.context_data["categories"] = ShopModels.Category.objects.filter(product_count__gte=1, business_count__gte=1)
        self.context_data["institutions"] = IdentityModels.Institution.objects.all()
        self.context_data["businesses"] = [
            {
                "business": business,
                'categories': [ category.category for category in ShopModels.BusinessCategory.objects.filter(business=business) ]
            } for business in (
                    lambda business: random.sample(business, len(business))
                )(list(ShopModels.Business.objects.all()))[:8]
        ]
        self.context_data["products"] = [
            {
                "product": product,
                "images": ShopModels.ProductImage.objects.filter(product=product)[:2]
            } for product in (
                    lambda products: random.sample(products, len(products))
                )(list(ShopModels.Product.objects.all().order_by("-id")))[:15]
        ]

        return render(request, template_name=self.template_name, context=self.context_data)

class ProductListView(View):
    template_name = "shop/product_list.html"
    context_data = {}
    model = ShopModels.Product

    def get(self, request):
        self.context_data["categories"] = ShopModels.Category.objects.filter(product_count__gte=1, business_count__gte=1)

        self.context_data["products"] = [
            {
                "product": product,
                "images": ShopModels.ProductImage.objects.filter(product=product)[:2]
            } for product in (
                    lambda products: random.sample(products, len(products))
                )(list(self.get_queryset()))[:15]
        ]
        return render(request, template_name=self.template_name, context=self.context_data)
    
    def get_queryset(self):
        search = self.request.GET.get("search", 0)
        if search:
            return self.model.objects.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(business__name__icontains=search) |
                Q(category__name__icontains=search) 
            ).order_by("-id")

        category = self.request.GET.get("category", 0)
        if category:
            return self.model.objects.filter(category__name=category).order_by("-id")

        return self.model.objects.all().order_by("-id")
class ProductDetailView(View):
    template_name = "shop/product_details.html"
    context_data = {}

    def get(self, request, slug):
        product = ShopModels.Product.objects.filter(slug=slug)
        if not product:
            return redirect(reverse_lazy("shop:error-page"))

        product = product.first()

        self.context_data["product"] = {
            "product": product,
            "images": ShopModels.ProductImage.objects.filter(product=product)
        }
        
        self.context_data["related_products"] = [
            {
                "product": product,
                "images": ShopModels.ProductImage.objects.filter(product=product)[:2]
            } for product in (
                    lambda products: random.sample(products, len(products))
                )(list(ShopModels.Product.objects.filter(
                    ~Q(pk = product.pk),
                    Q(category = product.category) |
                    Q(business = product.business)
                ).order_by("-id")))[:10]
        ]
        return render(request, template_name=self.template_name, context=self.context_data)

class BusinessListView(View):
    template_name = "shop/business_list.html"
    context_data = {}
    model = ShopModels.Business

    def get(self, request):
        self.context_data["categories"] = ShopModels.Category.objects.filter(product_count__gte=1, business_count__gte=1)
        self.context_data["businesses"] = [
            {
                "business": business,
                'categories': [ category.category for category in ShopModels.BusinessCategory.objects.filter(business=business) ]
            } for business in (
                    lambda business: random.sample(business, len(business))
                )(list(self.get_queryset()))[:8]
        ]
        return render(request, template_name=self.template_name, context=self.context_data)
    
    def get_queryset(self):
        category = self.request.GET.get("category", 0)
        queryset = []
        if not category:
            queryset = self.model.objects.all().order_by("-id")
        else:
            category = ShopModels.Category.objects.filter(name=category)
            if not category:
                return queryset
            
            for category_link in category.first().businesscategory_set.all():
                queryset.append(category_link.business)

        return queryset

class BusinessDetailView(View):
    template_name = "shop/business_details.html"
    context_data = {}

    def get(self, request, slug):
        business = ShopModels.Business.objects.filter(slug=slug)
        if not business:
            return redirect(reverse_lazy("shop:error-page"))

        business = business.first()

        self.context_data["business"] = {
            "business": business,
            'categories': [ category.category for category in ShopModels.BusinessCategory.objects.filter(business=business) ]
        }
        
        self.context_data["products"] = [
            {
                "product": product,
                "images": ShopModels.ProductImage.objects.filter(product=product)[:2]
            } for product in (
                    lambda products: random.sample(products, len(products))
                )(list(ShopModels.Product.objects.filter(business=business).order_by("-id")))[:10]
        ]
        return render(request, template_name=self.template_name, context=self.context_data)
    
class CartOrdersView(View):
    template_name = "shop/cart.html"
    context_data = {}

    def get(self, request):
        # user must be logged in
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("identity:login"))
        
        # if user has no cart, create a new cart
        cart = ShopModels.Cart.objects.filter(user=request.user)
        if not cart:
            cart = ShopModels.Cart.objects.create(
                user=request.user,
                total_amount=0.0
            )
        else:
            cart = cart.first()


        self.context_data["cart"] = cart
        # pass cart products
        self.context_data["cart_products"] = [
            {
                "product": cart_link,
                "image": ShopModels.ProductImage.objects.filter(product=cart_link.product).first()
            } for cart_link in cart.cartproduct_set.all()
        ]

        # pass orders
        orders = ShopModels.Order.objects.filter(buyer=request.user)

        total_amount = 0
        for order in orders:
            total_amount = decimal.Decimal(total_amount) + order.total_amount

        self.context_data["orders"] = {
            "total_amount": total_amount,
            "orders": [
                {
                    "order": order,
                    "image": ShopModels.ProductImage.objects.filter(product=order.product).first()
                } for order in orders
            ]
        }

        return render(request, template_name=self.template_name, context=self.context_data)
    
class CartToOrderView(View):
    template_name = "shop/cart.html"
    context_data = {}

    def post(self, request):
        # user must be logged in
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("identity:login"))
        
        # if user has no cart, show an error message
        cart = ShopModels.Cart.objects.filter(user=request.user)
        if not cart:
            messages.add_message(request, messages.ERROR, "Product not in cart.")
            return redirect(reverse_lazy("shop:cart"))
        cart = cart.first()

        # convert cart items to order and notify sellers
        cart.place_order()
        messages.add_message(request, messages.SUCCESS, "Order(s) placed successfully.")
        return redirect(reverse_lazy("shop:cart"))
    
class AddProductToCartView(View):
    template_name = "shop/cart.html"
    context_data = {}

    def get(self, request, slug):

        # user must be logged in
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("identity:login"))

        product = ShopModels.Product.objects.filter(slug=slug)
        if not product:
            return redirect(reverse_lazy("shop:error-page"))

        product = product.first()

        # user cannot add his own products to his cart
        if product.business.owner == request.user:
            messages.add_message(request, messages.ERROR, "You cannot buy from your shop.")
            return redirect(reverse_lazy("shop:product-list"))

        # get existing cart and add item
        # if user has no cart, create a new cart

        cart = ShopModels.Cart.objects.filter(user=request.user)
        if not cart:
            cart = ShopModels.Cart.objects.create(
                user=request.user,
                total_amount=0.0
            )
        else:
            cart = cart.first()

        # check if product is already in cart
        if ShopModels.CartProduct.objects.filter(cart = cart,product = product):
            messages.add_message(request, messages.ERROR, "Product is already in cart.")
            return redirect(reverse_lazy("shop:cart"))

        # add product to cart
        ShopModels.CartProduct.objects.create(
            cart = cart,
            product = product
        )
        
        return redirect(reverse_lazy("shop:cart"))


class DeleteProductToCartView(View):
    template_name = "shop/cart.html"
    context_data = {}

    def post(self, request, slug):

        # user must be logged in
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("identity:login"))

        product = ShopModels.Product.objects.filter(slug=slug)
        if not product:
            return redirect(reverse_lazy("shop:error-page"))
        product = product.first()

        # get existing cart and add item
        # if user has no cart, create a new cart

        cart = ShopModels.Cart.objects.filter(user=request.user)
        if not cart:
            messages.add_message(request, messages.ERROR, "Product not in cart.")
            return redirect(reverse_lazy("shop:cart"))
        cart = cart.first()

        # check if product is in cart\
        cart_link = ShopModels.CartProduct.objects.filter(cart = cart,product = product)
        if not cart_link:
            messages.add_message(request, messages.ERROR, "Product not in cart.")
            return redirect(reverse_lazy("shop:cart"))
        
        # remove product from cart
        cart_link.first().delete()
        return redirect(reverse_lazy("shop:cart"))