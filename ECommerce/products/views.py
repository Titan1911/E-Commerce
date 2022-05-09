from django.shortcuts import render
from .models import Product, ProductImage
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def show_all(request):
    if request.method=='POST':
        # add to cart
        print('the function is called')
        product_id = request.POST.get('product')
        user = request.user
        # print(user)
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get_or_create(user=user)
        # print(cart[0].id)
        cart_item = CartItem.objects.create(cart=cart[0], product=product)
        # when create is called, signal is called so no need to save this
        products = Product.objects.all()
        context = {'products':products}
        return render(request, 'products.html', context=context)
    
    elif request.method=='GET':   
        products = Product.objects.all()
        context = {'products':products}
        return render(request, 'products.html', context=context)

@login_required
def detail_view(request, id):
    product = Product.objects.get(id=id)
    photos = ProductImage.objects.filter(product=product)
    context = {'product': product, 'photos': photos}
    return render(request, 'details.html', context=context)

