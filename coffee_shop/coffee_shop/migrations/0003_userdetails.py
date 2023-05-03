# Generated by Django 4.2 on 2023-04-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0002_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]