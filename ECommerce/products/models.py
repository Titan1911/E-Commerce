from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,blank=True) # particular category which we get from url parameter

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.category_name 
    
    class Meta:
        db_table='category_table' # overriding the default database table name which will be 'name of the class' otherwise

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

class Product(models.Model):
    product_name = models.CharField(verbose_name="Product Name",max_length=50) # this is a verbose name, if the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE) # one to many field
    image = models.ImageField(upload_to='static/products')
    price = models.CharField(max_length=20, default='0')
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=100)
    # models.PROTECT will not delete the parent product,,
    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(ColorVariant, blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table='product_table' # overriding the default database table name which will be 'name of the class' otherwise