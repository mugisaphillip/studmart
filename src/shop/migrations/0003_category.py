# Generated by Django 5.0.6 on 2024-07-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_businessinstitution'),
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
    ]
