# Generated by Django 5.0.6 on 2024-07-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0009_institution_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tel_number',
            field=models.CharField(default=1, max_length=256, verbose_name='Tel number'),
            preserve_default=False,
        ),
    ]