from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.home, name='cart_home'),
    path('add/<slug:product_slug>/', views.add, name='add_to_cart'),
    path('remove/<slug:product_slug>/', views.remove, name='remove_from_cart'),
    path('delete/<slug:product_slug>/', views.delete, name='delete_from_cart'),
]