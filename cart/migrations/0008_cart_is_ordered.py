# Generated by Django 4.0.3 on 2022-07-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
