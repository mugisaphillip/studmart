from django.db import models
from django.utils.text import slugify
from identity import models as IdentityModels
from django.utils import timezone

import os
import uuid
import decimal

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s-%s.%s" % (instance, uuid.uuid4(), ext)
    return os.path.join(f"{instance.__class__.__name__}/images/", filename)

class Business(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    description = models.TextField("Description")
    owner = models.ForeignKey(to=IdentityModels.User, on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True)
    image = models.FileField(
        verbose_name="Image",
        upload_to=get_file_path,
    )
    created_on = models.DateField("Created on", default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # delete all business category relationships
        for rel in self.businesscategory_set.all():
            rel.delete()
        super(Business, self).delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class BusinessInstitution(models.Model):
    business = models.ForeignKey(to=Business, on_delete=models.CASCADE, null=False, blank=False)
    institution = models.ForeignKey(to=IdentityModels.Institution, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.business} - {self.institution}'
    
class Category(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    product_count = models.IntegerField(verbose_name="Product count", default=0)
    business_count = models.IntegerField(verbose_name="Product count", default=0)

    def __str__(self) -> str:
        return f'{self.name}. Products:{self.product_count} Businesses: {self.business_count}'

class BusinessCategory(models.Model):
    business = models.ForeignKey(to=Business, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=False, blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.category.business_count += 1
        self.category.save()

    def delete(self, *args, **kwargs):
        super(BusinessCategory, self).delete(*args, **kwargs)
        self.category.business_count -= 1
        self.category.save()

    def __str__(self) -> str:
        return f'{self.business} - {self.category}'
    
class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    description = models.TextField("Description")
    stock = models.IntegerField(verbose_name="stock", default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=False, blank=False)
    price = models.DecimalField(verbose_name="price", decimal_places=2, max_digits=10)
    business = models.ForeignKey(to=Business, on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True)
    created_on = models.DateField("Created on", default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        self.category.product_count += 1
        self.category.save()

    def delete(self, *args, **kwargs):
        super(Product, self).delete(*args, **kwargs)
        self.category.product_count -= 1
        self.category.save()
    
    def __str__(self) -> str:
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False, blank=False)
    image = models.FileField(
        verbose_name="Image",
        upload_to=get_file_path,
    )
    def __str__(self) -> str:
        return self.product.name
    


class Order(models.Model):
    order_status = (
        ("PENDING", "PENDING"),
        ("ACCEPTED", "ACCEPTED"),
        ("COMPLETE", "COMPLETE"),
    )

    buyer = models.ForeignKey(to=IdentityModels.User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(verbose_name="quantity", default=1)
    status = models.CharField(verbose_name="status", choices=order_status, default="PENDING", max_length=100)
    created_on = models.DateField("Created on", default=timezone.now)
    completed_on = models.DateField("Completed on", null=True, blank=True)

class Cart(models.Model):
    user = models.ForeignKey(to=IdentityModels.User, on_delete=models.CASCADE, null=False, blank=False)
    total_amount = models.DecimalField(verbose_name="total amount", decimal_places=2, max_digits=10)
    product_count = models.IntegerField(verbose_name="Product count", default=0)

    def __str__(self) -> str:
        return self.user.username

    def place_order(self, *args, **kwargs):
        orders = []
        for product  in self.cartproduct_set.all():
            order = Order.objects.create(
                buyer = self.user,
                product = product.product,
                quantity = product.quantity
            )
            orders.append(order)

        # clear cart
        self.delete()
        return orders
    
class CartProduct(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, null=False, blank=False)
    total_amount = models.DecimalField(verbose_name="total amount", decimal_places=2, max_digits=10)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(verbose_name="quantity", default=1)

    def save(self, *args, **kwargs):
        self.total_amount = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.cart.product_count += 1
        self.cart.total_amount = decimal.Decimal(self.cart.total_amount)+ decimal.Decimal(self.total_amount)
        self.cart.save()

    def delete(self, *args, **kwargs):
        super(CartProduct, self).delete(*args, **kwargs)
        self.cart.product_count -= 1
        self.cart.total_amount = decimal.Decimal(self.cart.total_amount) - decimal.Decimal(self.total_amount)
        self.cart.save()