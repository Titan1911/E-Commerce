from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, editable=False) # particular category which we get from url parameter

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.category_name 
    
    class Meta:
        db_table='category_table' # overriding the default database table name which will be 'name of the class' otherwise

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.size_name

class Product(models.Model):
    product_name = models.CharField(verbose_name="Product Name", max_length=50) # this is a verbose name, 
    # if the verbose name isn’t given, Django will automatically create it using the field’s attribute name, 
    # converting underscores to spaces.
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # one to many field
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=100)
    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    color_type = models.ForeignKey(ColorVariant, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    size_type = models.ForeignKey(SizeVariant, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table='product_table' # overriding the default database table name which will be 'name of the class' otherwise

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/')

    def __str__(self) -> str:
        return str(self.product.product_name)


# this signal if for when there is an updation in the products then delete all the cache related to products page
@receiver(post_save, sender=Product)
def product_updation(sender, **kwargs):
    cache.delete_pattern('products')
    cache.delete_pattern('product.*')
    cache.delete_pattern('photos.*')
    cache.delete_pattern('categories')
    cache.delete_pattern('category.*')

@receiver(post_delete, sender=Product)
def product_deletion(sender, **kwargs):
    cache.delete_pattern('products')
    cache.delete_pattern('product.*')
    cache.delete_pattern('photos.*')
    cache.delete_pattern('categories')
    cache.delete_pattern('category.*')

@receiver(post_save, sender=Category)
def category_updation(sender, **kwargs):
    cache.delete_pattern('categories')
    cache.delete_pattern('category.*')

@receiver(post_delete, sender=Category)
def category_deletion(sender, **kwargs):
    cache.delete_pattern('categories')
    cache.delete_pattern('category.*')
