from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.user.username)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0, editable=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product.product_name)


# make sure whenever the Model.objects.create() function is called, the signal is called
@receiver(pre_save, sender=CartItem, dispatch_uid="my_unique_identifier") # this task is done before saving
def correct_price(sender, **kwargs):
    print('pre signal called')
    cart_items = kwargs['instance']
    print(kwargs)
    object = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(object.price)
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price += cart_items.price
    cart.save()

@receiver(post_save, sender=CartItem) # this task is done after saving
def total_items(sender, **kwargs):
    print('post signal called')
    cart_items = kwargs['instance']
    cart = Cart.objects.get(id=cart_items.cart.id)
    total_items = CartItem.objects.filter(cart__user=cart.user).count()
    cart.total_items = total_items
    cart.save()

