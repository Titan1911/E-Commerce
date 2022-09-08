from django import template
from cart.models import Cart, CartItem

register = template.Library()

@register.simple_tag(takes_context=True)
def is_in_cart(context):
    request = context['request']
    user = request.user
    product = context['product']
    cart = Cart.objects.get_or_create(user=user)
    try:
        product_quantity = CartItem.objects.get(product=product.id, cart=cart[0].id).quantity
        return product_quantity
    except:
        return 0
