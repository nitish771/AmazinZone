from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
	path('', views.store, name='home'),
	path('category/<slug:category_slug>', views.category, name='category'),
	path('category/all/', views.category_all, name='category_all'),
]
