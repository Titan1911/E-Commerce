# Generated by Django 4.0.3 on 2022-04-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total_items',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]
