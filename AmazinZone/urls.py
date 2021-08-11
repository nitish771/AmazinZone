from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'amazinzone'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('store/', include('store.urls'), name="store"),
    path('products/', include('products.urls'), name="products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
