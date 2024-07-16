from django.test import TestCase
from identity import models

# user profile models tests
class UserTestCase(TestCase):
    def setUp(self):
        models.User.objects.create(
            first_name="phillip",
            surname="mugisa",
            username="mugisaphillip",
            isdelivery=True,
            password="Mugisa1234"
        )

    def test_user_created(self):
        phillip = models.User.objects.first()
        self.assertTrue(phillip)

    def test_user_delivery_mode(self):
        phillip = models.User.objects.first()
        self.assertTrue(phillip.isdelivery)

        phillip.isdelivery = False
        phillip.save()
        self.assertFalse(phillip.isdelivery)

    def test_default_user_account_type(self):
        phillip = models.User.objects.first()
        self.assertTrue(phillip.account_type)
        self.assertEqual(phillip.account_type, "BUYER")

    def test_user_account_type(self):
        phillip = models.User.objects.first()
        phillip.account_type = "SELLER"
        phillip.save()
        self.assertEqual(phillip.account_type, "SELLER")

    def test_default_user_institution(self):
        phillip = models.User.objects.first()
        self.assertFalse(phillip.institution)

class InstituionTestCase(TestCase):
    def test_create_institution(self):
        mak = models.Institution(
            name="Makerere",
            abbr="Mak",
            location='Makerere'
        )
        mak.save()
        self.assertTrue(mak)
    
    def test_add_user_to_institution(self):
        user = models.User.objects.create(
            first_name="phillip",
            surname="mugisa",
            username="mugisaphillip",
            isdelivery=True,
            password="Mugisa1234"
        )
        
        mak = models.Institution.objects.create(
            name="Makerere",
            abbr="Mak",
            location='Makerere'
        )

        self.assertFalse(user.institution) # institution is not set yet
        user.institution = mak
        user.save()
        self.assertEqual(user.institution, mak)

    def test_institution_has_slug(self):
        mak = models.Institution(
            name="Makerere",
            abbr="Mak",
            location='Makerere'
        )
        mak.save()
        self.assertTrue(mak.slug)