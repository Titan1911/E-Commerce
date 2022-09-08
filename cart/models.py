from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from products.models import Product
from django.db.models import Max, Min, Count, Sum

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    is_ordered = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.user.username)

    def save(self, *args, **kwargs):
        if self.is_ordered==True:
            self.delete()
        else:
            return super(Cart, self).save(*args, **kwargs)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.product_name)


# make sure whenever the Model.objects.create() or .save() function is called, the signal is called
# @receiver(pre_save, sender=CartItem) # this task is done before saving
# def correct_price(sender, **kwargs):
#     print('pre signal called')
#     cart_item = kwargs['instance']
#     # print(kwargs)
#     product = Product.objects.get(id=cart_item.product.id)
#     cart_item.price = cart_item.quantity * float(product.price)
#     cart = Cart.objects.get(id=cart_item.cart.id)
#     cart.total_price = float(product.price)
#     cart.save()

# @receiver(post_save, sender=CartItem) # this task is done after saving
# def total_items(sender, **kwargs):
#     print('post signal called')
#     cart_item = kwargs['instance']
#     cart = Cart.objects.get(id=cart_item.cart.id)
#     total_items = CartItem.objects.aggregate(Sum('quantity'))
#     print(cart.total_items)
#     cart.total_items = total_items['quantity__sum']
#     print(cart.total_items)
#     cart.save()
