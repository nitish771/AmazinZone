from django.shortcuts import render
from django.views.generic import ListView

from . import models


def store(request, **kwargs):
	categories = models.Category.objects.all()
	category_products = models.Product.objects.all()

	args = {
		'categories': categories,
		'category_products': category_products
	}

	try:
		args.update(kwargs.get('context'))
	except:
		pass
	return render(request, 'store.html', context=args)


def category_all(request):
	return store(request, template_name='store.html')


def category(request, category_slug):
	category_products = models.Product.objects.filter(category__slug=category_slug)
	return store(request, template_name='store.html',
		context={'category_products': category_products})
