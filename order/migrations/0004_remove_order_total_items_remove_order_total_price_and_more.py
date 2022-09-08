# Generated by Django 4.0.3 on 2022-07-10 20:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cart_is_ordered'),
        ('order', '0003_remove_order_items_order_total_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cart.cartitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
