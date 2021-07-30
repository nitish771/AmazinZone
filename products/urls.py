from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
	path('', views.home, name='home'),
	path('<slug:slug>/', views.Detail.as_view(), name='product_detail'),
]
