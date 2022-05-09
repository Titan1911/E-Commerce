from django.shortcuts import render
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def show_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(cart__user=user)
    cart = Cart.objects.get(user=user)
    context = {'cart_items': cart_items, 'cart': cart}
    return render(request, 'cart.html', context=context)


    