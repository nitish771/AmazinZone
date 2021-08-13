
from .models import CartItem
from .views import _cart_id

    
def grand_total(request, tax_rate=6.9):
    grand_total = 0
    total = 0
    cart_items = CartItem.objects.filter(cart__cart_id=_cart_id(request))
    for item in cart_items:
        print(item, item.sub_total())
        total += item.sub_total()
    tax = total*tax_rate//100

    context = {}
    context['cart_total'] = total
    context['cart_tax'] = tax
    context['cart_tax_rate'] = tax_rate
    context['grand_total'] = tax+total
    return context
