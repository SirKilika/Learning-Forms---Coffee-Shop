# Generated by Django 4.2 on 2023-04-29 20:22

import coffee_shop.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0003_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='phone',
            field=models.CharField(default=9100000000, max_length=100, validators=[django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='zipcode',
            field=models.CharField(default=0, max_length=10, validators=[coffee_shop.validators.validate_zipcode]),
            preserve_default=False,
        ),
    ]