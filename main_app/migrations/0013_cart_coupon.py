# Generated by Django 2.1.1 on 2018-10-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20181010_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.FloatField(default=1),
        ),
    ]
