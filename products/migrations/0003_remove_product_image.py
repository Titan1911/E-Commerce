# Generated by Django 4.0.3 on 2022-04-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_productimages_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
