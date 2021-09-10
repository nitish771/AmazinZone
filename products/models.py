from django.db import models
from django.utils import timezone

from store.models import Product


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def color(self):
        return super(VariationManager, self).filter(active=True, variation_type='colors')

    def size(self):
        return super(VariationManager, self).filter(active=True, variation_type='sizes')


VAR_CHOICES = [
    ('sizes', 'size'),  # (first will use, second will show in admin panel)
    ('colors', 'color'),
]

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_type = models.CharField(max_length=120, choices=VAR_CHOICES,
            default='size')
    variation_value = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products/variations/', blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(default=timezone.now)

    objects = VariationManager()

    def __str__(self):
        return self.product.title

