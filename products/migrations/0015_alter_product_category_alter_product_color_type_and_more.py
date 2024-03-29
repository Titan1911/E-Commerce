# Generated by Django 4.0.3 on 2022-07-31 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_color_type_alter_product_quantity_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.quantityvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.sizevariant'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.product'),
        ),
    ]
