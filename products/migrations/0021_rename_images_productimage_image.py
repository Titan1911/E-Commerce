# Generated by Django 4.0.8 on 2023-01-01 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_productimage_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='images',
            new_name='image',
        ),
    ]
