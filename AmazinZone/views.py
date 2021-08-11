from django.shortcuts import render
from django.views.generic import TemplateView

from store.models import Product, Category


def homepage(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'homepage_products': products})