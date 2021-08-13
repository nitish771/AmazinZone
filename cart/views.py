from django.shortcuts import render, redirect
from django.http import Http404

from .models import Cart, CartItem
from store.models import Product


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def home(request):
    cart_items = CartItem.objects.all()
    print(cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items})


def get_cart_variables(request, product_slug):
    var_dict = {}
    product = Product.objects.get(slug=product_slug)
    current_user = request.user
    var_dict['product'] = product
    var_dict['current_user'] = current_user

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    var_dict['cart'] = cart
    return var_dict


def add(request, product_slug):
    variables = get_cart_variables(request, product_slug)
    product = variables.get('product')
    current_user = variables.get('current_user')
    cart = variables.get('cart')

    if current_user.is_authenticated:
        # increase or add in cart
        try:
            cart_item = CartItem.objects.get(product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(product=product, cart=cart)
    return redirect('cart:cart_home')        


def delete(request, product_slug):
    variables = get_cart_variables(request, product_slug)
    product = variables.get('product')
    current_user = variables.get('current_user')
    cart = variables.get('cart')

    if current_user.is_authenticated:
        # delete from in cart
        try:
            cart_item = CartItem.objects.get(product=product).delete()
        except CartItem.DoesNotExist:
            return Http404
    return redirect('cart:cart_home')        


def remove(request, product_slug):
    variables = get_cart_variables(request, product_slug)
    product = variables.get('product')
    current_user = variables.get('current_user')
    cart = variables.get('cart')

    if current_user.is_authenticated:
        # decrease or remove from cart
        try:
            cart_item = CartItem.objects.get(product=product)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item = CartItem.objects.get(product=product).delete()
        except CartItem.DoesNotExist:
            return Http404
    return redirect('cart:cart_home')        


