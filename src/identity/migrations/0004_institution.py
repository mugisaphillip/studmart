# Generated by Django 5.0.6 on 2024-07-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0003_user_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('abbr', models.CharField(max_length=256, verbose_name='Abbr')),
                ('location', models.CharField(max_length=256, verbose_name='location')),
            ],
        ),
    ]
