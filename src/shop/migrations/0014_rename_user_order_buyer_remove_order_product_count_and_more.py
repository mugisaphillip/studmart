# Generated by Django 5.0.6 on 2024-07-16 13:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_cartproduct_quantity_cartproduct_total_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='buyer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_count',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='business',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created on'),
        ),
        migrations.AddField(
            model_name='order',
            name='completed_on',
            field=models.DateField(blank=True, null=True, verbose_name='Completed on'),
        ),
        migrations.AddField(
            model_name='order',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created on'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('COMPLETE', 'COMPLETE')], default='PENDING', max_length=100, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created on'),
        ),
    ]
