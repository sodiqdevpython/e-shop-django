# Generated by Django 3.2.15 on 2024-05-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eShopApp', '0009_shipping_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
