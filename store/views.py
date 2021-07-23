from django.shortcuts import render
from django.views.generic import ListView

from . import models


class Store(ListView):
	template_name = 'store.html'
	model = models.Product

	context_object_name = 'products_list'
