from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils import timezone

import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s-%s.%s" % (instance, uuid.uuid4(), ext)
    return os.path.join(f"{instance.__class__.__name__}/images/", filename)

class User(AbstractUser):
    account_types = (
        ("BUYER", "BUYER"),
        ("SELLER", "SELLER"),
        ("SUPPORT", "SUPPORT"),
    )

    surname = models.CharField(verbose_name="Surname", max_length=256)
    tel_number = models.CharField(verbose_name="Tel number", max_length=256, null=True, blank=True)
    isdelivery = models.BooleanField(verbose_name="Is a delivery agent", default=False)
    account_type = models.CharField(verbose_name="account type", choices=account_types, default="BUYER", max_length=100)
    institution = models.ForeignKey(to="Institution", on_delete=models.SET_NULL, null=True, blank=True)
    
    image = models.FileField(
        verbose_name="Image",
        upload_to=get_file_path,
        default="user/user.png",
    )
    
    def __str__(self):
        return f"{self.username}"

class Institution(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    abbr = models.CharField(verbose_name="Abbr", max_length=256)
    location = models.CharField(verbose_name="location", max_length=256)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True)
    created_on = models.DateField("Created on", default=timezone.now)
    
    image = models.FileField(
        verbose_name="Image",
        upload_to=get_file_path,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
