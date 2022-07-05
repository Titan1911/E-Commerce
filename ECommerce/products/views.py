from venv import create
from django.shortcuts import render
from .models import Product, ProductImage
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def show_all(request):
    if request.method=='POST':
        # add to cart
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        user = request.user
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get_or_create(user=user)
        item = CartItem.objects.get_or_create(product=product, cart=cart[0])
        cart_item = item[0]
        cart = cart[0]
        print(cart.total_price)
        # print(remove)
        if remove:
            cart_item.quantity-=1
            cart_item.save()
            cart.total_items-=1
            cart.total_price -= product.price
            cart.save()
            if cart_item.quantity==0:
                cart_item.delete()
        else:
            cart_item.quantity+=1
            # if created==False:
            cart_item.price = cart_item.quantity * float(product.price)
            cart_item.save()
            # cart_item.save() # when create is called, signal is called so no need to save this
            print(cart_item.price,'this is cart_item.price')
            cart.total_items+=1
            cart.total_price += product.price
            cart.save()
        products = Product.objects.all()
        cart_items = CartItem.objects.all()
        context = {'products':products, 'cart_items':cart_items}
        return render(request, 'products.html', context=context)
    
    elif request.method=='GET':   
        products = Product.objects.all()
        cart_items = CartItem.objects.all()
        context = {'products':products, 'cart_items':cart_items}
        return render(request, 'products.html', context=context)

@login_required
def detail_view(request, id):
    product = Product.objects.get(id=id)
    photos = ProductImage.objects.filter(product=product)
    context = {'product': product, 'photos': photos}
    return render(request, 'details.html', context=context)

