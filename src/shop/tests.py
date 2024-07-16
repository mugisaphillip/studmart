from django.test import TestCase
from shop import models
from identity import models as IdentityModels

class BusinessTestCase(TestCase):
    def setUp(self):
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
        
        models.Business.objects.create(
            name="Stono",
            owner = user,
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
        )
        
    def test_create_business(self):
        self.assertTrue(models.Business.objects.first())

    def test_category_create(self):
        shoes = models.Category.objects.create(name="Shoes")
        self.assertTrue(shoes)
        self.assertEqual(shoes.product_count, 0)
        self.assertEqual(shoes.business_count, 0)

    def test_add_business_categories(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")
        phones = models.Category.objects.create(name="phones")

        models.BusinessCategory.objects.create(
            business = business,
            category= shoes
        )
        self.assertEqual(business.businesscategory_set.first().category.name, "Shoes")

        models.BusinessCategory.objects.create(
            business = business,
            category= phones
        )

        self.assertEqual(len(business.businesscategory_set.all()), 2)

    def test_business_categories_count_increase(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")
        phones = models.Category.objects.create(name="phones")

        models.BusinessCategory.objects.create(
            business = business,
            category= shoes
        )
        self.assertEqual(shoes.business_count, 1)
        self.assertEqual(phones.business_count, 0)

    def test_business_categories_count_decrease(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")

        models.BusinessCategory.objects.create(
            business = business,
            category= shoes
        )
        self.assertEqual(shoes.business_count, 1)

        # on business delete
        business.delete()
        self.assertEqual(models.Category.objects.first().business_count, 0)

    def test_add_business_to_institution(self):
        mak = IdentityModels.Institution.objects.first()
        business = models.Business.objects.first()

        # business can operate in many institutions
        models.BusinessInstitution.objects.create(
            institution=mak,
            business=business
        )

        link = business.businessinstitution_set.first()
        self.assertEqual(mak, link.institution)
        self.assertEqual(business, link.business)


class ProductTestCase(TestCase):
    def setUp(self):
        user = IdentityModels.User.objects.create(
            first_name="phillip",
            surname="mugisa",
            username="mugisaphillip",
            isdelivery=True,
            password="Mugisa1234"
        )
        models.Business.objects.create(
            name="Stono",
            owner = user,
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
        )

    def test_product_create(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")

        product = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )

        self.assertEqual(product, models.Product.objects.first())

    def test_product_category_count_increase(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")

        self.assertEqual(shoes.product_count, 0)
        models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )

        self.assertEqual(shoes.product_count, 1)

    def test_product_category_count_decrease(self):
        business = models.Business.objects.first()
        shoes = models.Category.objects.create(name="Shoes")

        self.assertEqual(shoes.product_count, 0)
        product = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )
        self.assertEqual(shoes.product_count, 1)

        product.delete()
        self.assertEqual(shoes.product_count, 0)

class CartTestCase(TestCase):
    def setUp(self):
        user = IdentityModels.User.objects.create(
            first_name="phillip",
            surname="mugisa",
            username="mugisaphillip",
            isdelivery=True,
            password="Mugisa1234"
        )
        
        models.Business.objects.create(
            name="Stono",
            owner = user,
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
        )

    def test_cart_create(self):
        user = IdentityModels.User.objects.first()

        cart = models.Cart.objects.create(
            user=user,
            total_amount=0.0
        )
        self.assertEqual(cart, models.Cart.objects.filter(user=user).first())
        self.assertEqual(cart.product_count, 0)

    def test_add_to_cart(self):
        shoes = models.Category.objects.create(name="Shoes")
        phones = models.Category.objects.create(name="Phones")
        business = models.Business.objects.first()
        user = IdentityModels.User.objects.first()

        product_1 = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )
        product_2 = models.Product.objects.create(
            name="Iphone 15",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=3000000.0,
            stock=100,
            category=phones
        )

        cart = models.Cart.objects.create(
            user=user,
            total_amount=0.0
        )

        cart_item_1 = models.CartProduct.objects.create(
            cart = cart,
            product = product_1
        )

        self.assertEqual(cart.product_count, 1)
        self.assertEqual(cart.total_amount, cart_item_1.product.price)

        
        cart_item_2 = models.CartProduct.objects.create(
            cart = cart,
            product = product_2
        )
        self.assertEqual(cart.product_count, 2)
        self.assertEqual(cart.total_amount, cart_item_1.product.price + cart_item_2.product.price)

    def test_add_to_cart_with_varied_quantity(self):
        shoes = models.Category.objects.create(name="Shoes")
        business = models.Business.objects.first()
        user = IdentityModels.User.objects.first()

        product_1 = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )

        cart = models.Cart.objects.create(user=user,total_amount=0.0)

        cart_item_1 = models.CartProduct.objects.create(cart = cart,product = product_1, quantity=5)

        self.assertEqual(cart.product_count, 1)
        self.assertEqual(cart.total_amount, cart_item_1.product.price * 5)

    def test_cart_remove(self):
        shoes = models.Category.objects.create(name="Shoes")
        business = models.Business.objects.first()
        user = IdentityModels.User.objects.first()

        product_1 = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )

        cart = models.Cart.objects.create(
            user=user,
            total_amount=0.0
        )

        cart_item = models.CartProduct.objects.create(
            cart = cart,
            product = product_1
        )

        self.assertEqual(cart.product_count, 1)
        self.assertEqual(cart.total_amount, cart_item.product.price)

        # remove product
        cart_item.delete()

        self.assertEqual(cart.product_count, 0)
        self.assertEqual(cart.total_amount, 0.0)

    def test_cart_to_order(self):
        
        shoes = models.Category.objects.create(name="Shoes")
        phones = models.Category.objects.create(name="Phones")
        business = models.Business.objects.first()
        user = IdentityModels.User.objects.first()

        product_1 = models.Product.objects.create(
            name="Nike Air Force",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=150000.0,
            stock=100,
            category=shoes
        )
        product_2 = models.Product.objects.create(
            name="Iphone 15",
            description="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore alias incidunt inventore rem ratione dignissimos. Soluta error voluptate nostrum culpa!",
            business=business,
            price=3000000.0,
            stock=100,
            category=phones
        )

        cart = models.Cart.objects.create(user=user,total_amount=0.0)
        models.CartProduct.objects.create(cart = cart,product = product_1)
        models.CartProduct.objects.create(cart = cart,product = product_2)

        cart.place_order()
        
        # cart should be cleared
        self.assertEqual(len(models.Cart.objects.all()), 0)

        # orders must equal to products that were in cart
        orders = models.Order.objects.all()
        self.assertEqual(len(orders), 2)