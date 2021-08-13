from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'amazinzone'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('store/', include('store.urls'), name="store"),
    path('products/', include('products.urls'), name="products"),
    path('cart/', include('cart.urls'), name="cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
