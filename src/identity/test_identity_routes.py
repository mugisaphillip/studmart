from django.test import TestCase, Client
from django.urls import reverse
from shop import models as ShopModels
from identity import models as IdentityModels

class ShopRouteTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse("identity:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("identity/login.html")

        # user should be able to login in via post
        response = self.client.post(reverse("identity:login"), {"username": "mugisa", "password": "mugisa"})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.get(reverse("identity:logout"))
        self.assertEqual(response.status_code, 302) # redirects to login