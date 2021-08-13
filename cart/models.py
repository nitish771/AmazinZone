from django.db import models
from django.utils import timezone


from store.models import Product, Category


class Cart(models.Model):
    cart_id = models.CharField(max_length=100)
    cart_items_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def update_cart_items_count(self, add_n):
        print('incrementing ', add_n)
        self.cart_items_count += add_n

    def __str__(self):
        return self.cart_id



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title