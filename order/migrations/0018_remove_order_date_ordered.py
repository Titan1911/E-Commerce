# Generated by Django 4.0.3 on 2022-08-06 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_order_time_ordered_alter_order_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
    ]
