# Generated by Django 5.0.6 on 2024-07-16 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_user_institution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Institution',
            new_name='institution',
        ),
    ]