# Generated by Django 2.1.1 on 2018-10-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
