# Generated by Django 2.1.1 on 2018-10-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_cart_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount_amount',
            field=models.IntegerField(default=0),
        ),
    ]
