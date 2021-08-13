from .models import CartItem
from .views import _cart_id


def grand_total(request, tax_rate=6.9):
    total = 0
    count = 0
    cart_items = CartItem.objects.filter(cart__cart_id=_cart_id(request))
    for item in cart_items:
        total += item.sub_total()
        count += item.quantity
    tax = total * tax_rate // 100

    context = {}
    context['cart_items_count'] = count
    context['cart_total'] = total
    context['cart_tax'] = tax
    context['cart_tax_rate'] = tax_rate
    context['grand_total'] = tax + total
    return context
