# Generated by Django 5.0.6 on 2024-07-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_count',
            field=models.IntegerField(default=0, verbose_name='Product count'),
        ),
    ]
