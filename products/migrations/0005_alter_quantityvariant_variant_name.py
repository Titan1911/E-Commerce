# Generated by Django 4.0.3 on 2022-04-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_quantityvariant_variant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantityvariant',
            name='variant_name',
            field=models.IntegerField(),
        ),
    ]
