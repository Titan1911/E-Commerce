from itertools import product
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from products.models import Product
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


class Order(models.Model):
    CHOICE = [
    ('Ordered', 'Ordered'),
    ('Shipped', 'Shipped'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.IntegerField()
    total_items = models.IntegerField()
    date_ordered = models.DateField(auto_now_add=True, blank=True, null=True)
    time_ordered = models.TimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICE, default='Ordered', null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user.username)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.product.product_name)


@receiver(pre_save, sender=Order)
def Order_price_item(sender, **kwargs):
    order = kwargs['instance']
    user = order.user
    try:
        cart = Cart.objects.get(user=user)
        order.total_price = cart.total_price
        order.total_items = cart.total_items
    except:
        pass


@receiver(post_save, sender=Order)
def OrderItem_prices_items(sender, **kwargs):
    order = kwargs['instance']
    user = order.user
    cart_items = CartItem.objects.filter(cart__user=user)
    for e in cart_items:
        OrderItem.objects.create(
            order=order,
            product=e.product,
            price=e.price,
            quantity=e.quantity)
        product = Product.objects.get(id=e.product.id)
        product.stock-= e.quantity
        product.save()
    




