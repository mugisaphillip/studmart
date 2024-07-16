from django.test import TestCase, Client
from django.urls import reverse
from shop import models as ShopModels
from identity import models as IdentityModels

class ShopRouteTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        
        user = IdentityModels.User.objects.create(
            first_name="phillip",
            surname="mugisa",
            username="mugisaphillip",
            isdelivery=True,
            password="Mugisa1234"
        )

        IdentityModels.Institution.objects.create(
            name="Makerere",
            abbr="Mak",
            location='Makerere'
        )
        
        business = ShopModels.Business.objects.create(
            name="Stono",
            owner = user,
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
        )

        shoes = ShopModels.Category.objects.create(name="Shoes")
        phones = ShopModels.Category.objects.create(name="phones")

        ShopModels.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )
        ShopModels.Product.objects.create(
            name="Iphone 15",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=3000000.0,
            stock=100,
            category=phones
        )

    def test_home_route(self):
        response = self.client.get(reverse("shop:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/index.html")

    def test_product_list_route(self):
        response = self.client.get(reverse("shop:product-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_list.html")

    def test_product_detail_route(self):
        product = ShopModels.Product.objects.first()
        response = self.client.get(reverse("shop:product-details", args=[product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_details.html")

    def test_business_list_route(self):
        response = self.client.get(reverse("shop:business-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/business_list.html")

    def test_detail_detail_route(self):
        business = ShopModels.Business.objects.first()
        response = self.client.get(reverse("shop:business-details", args=[business.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/business_details.html")