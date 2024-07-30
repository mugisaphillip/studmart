# Generated by Django 5.0.6 on 2024-07-30 00:08

import django.db.models.deletion
import django.utils.timezone
import shop.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('identity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('product_count', models.IntegerField(default=0, verbose_name='Product count')),
                ('business_count', models.IntegerField(default=0, verbose_name='Product count')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('image', models.FileField(upload_to=shop.models.get_file_path, verbose_name='Image')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.business')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identity.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total amount')),
                ('product_count', models.IntegerField(default=0, verbose_name='Product count')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.business')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('stock', models.IntegerField(default=0, verbose_name='stock')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.business')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total amount')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('COMPLETED', 'COMPLETED'), ('DECLINED', 'DECLINED')], default='PENDING', max_length=100, verbose_name='status')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('completed_on', models.DateField(blank=True, null=True, verbose_name='Completed on')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total amount')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=shop.models.get_file_path, verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
