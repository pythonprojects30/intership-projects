from django.shortcuts import render, redirect, get_object_or_404
from cart_app.models import Cart, CartItem
from ecartapp.models import Product
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )

        cart.save(),

    try:
        cartitem=CartItem.objects.get(product=product,cart=cart)
        if cartitem.quantity < cartitem.product.stock:
            cartitem.quantity += 1

        cartitem.save(),
    except CartItem.DoesNotExist:
        cartitem=CartItem.objects.create(

            product=product,
            cart=cart,
            quantity=1
        )

        cartitem.save(),
    return  redirect('cart_app:cart_detail')

def cart_detail(request,total=0,counter=0,cartitems=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cartitems=CartItem.objects.filter(cart=cart,active=True)
        for cartitem in cartitems:
            total += (cartitem.product.price * cartitem.quantity)
            counter += cartitem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitem=cartitems,total=total,counter=counter))




def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(cart=cart,product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_detail')

def trash(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_app:cart_detail')