# Generated by Django 4.0.3 on 2022-04-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantityvariant',
            name='variant_name',
            field=models.IntegerField(max_length=100),
        ),
    ]
