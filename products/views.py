from django.shortcuts import render
from .models import Category, Product, ProductImage
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


@login_required
def show_all(request):
    if request.method=='POST':
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        user = request.user
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get_or_create(user=user)
        item = CartItem.objects.get_or_create(product=product, cart=cart[0])
        cart_item = item[0]
        cart = cart[0]
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
            cart.total_items += 1
            cart.total_price += product.price
            cart.save()
    
    if cache.get('categories'):
        categories = cache.get('categories')
    else:
        categories = Category.objects.all()
        cache.set('categories', categories)
    slug = request.GET.get('category')
    if slug:
        category_key = f'category.{slug}'
        if cache.get(category_key):
            products = cache.get(category_key)
        else:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category)
            cache.set(category_key, products)
    else:
        products_key = f'products'
        if cache.get(products_key):
            products = cache.get(products_key)
        else:
            products = Product.objects.all()
            cache.set(products_key, products)
    cart_items = CartItem.objects.all()
    context = { 'products':products, 'cart_items':cart_items, 'categories': categories }
    return render(request, 'products.html', context=context)


@login_required
def detail_view(request, id):
    product_key = f'product.{id}'
    photo_key = f'photos.{id}'
    if cache.get(product_key):
        product = cache.get(product_key)
    else:
        product = Product.objects.get(id=id)
        cache.set(f'product.{id}', product)
    if cache.get(photo_key):
        photos = cache.get(photo_key)
    else:
        photos = ProductImage.objects.filter(product=product)
        cache.set(f'photos.{id}', photos)
    context = {'product': product, 'photos': photos}
    return render(request, 'details.html', context=context)

