from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from store.models import Product



def home(request):
	return HttpResponse("Whcih product you are searching for")


class Detail(DetailView):
	template_name = 'product_detail.html'
	context_object_name = 'product_details'
	model = Product

