from tracemalloc import clear_traces
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # order = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return str(self.user.username) + " " + str(self.total_price)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)

@receiver(pre_save, sender=CartItem) # this task is done before saving
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    object = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(object.price)
    # total_cart_items = CartItem.objects.filter(user=cart_items.user)
    # cart_items.total_items = len(total_cart_items)
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()
    