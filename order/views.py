from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetail
from cart.models import Cart
from .models import Order, OrderItem


@login_required
def details(request):
    user = request.user
    user_details = UserDetail.objects.filter(user__username=user)
    if len(user_details)!=0:
        context = { 'user_details': user_details }
    else:
        context = {}
    return render(request, 'userdetails.html', context=context)

@login_required
def order(request):
    user = request.user
    if request.method=='POST':
        user_details = request.POST
        phone = user_details.get('phone')
        address = user_details.get('address')
        exists = user_details.get('existed_value')
        if exists=='False':
            if not ( phone=='' or address=='' ):
                userdetails = UserDetail.objects.create(user=user, address=address, phone=phone)
                userdetails.save()
        order = Order.objects.create(user=user)
        cart = Cart.objects.get(user=user)
        cart.is_ordered=True
        cart.save()
    orders = Order.objects.filter(user=user).order_by('-date_ordered', '-time_ordered')
    context = { 'orders': orders }
    return render(request, 'order.html', context=context)
        
@login_required
def ordered_items(request, id):
    order = Order.objects.get(id=id)
    ordered_items = OrderItem.objects.filter(order=order)
    context = { 'order': order, 'ordered_items': ordered_items }
    return render(request, 'ordered_items.html', context=context)