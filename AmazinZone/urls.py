from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'amazinzone'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage.as_view(), name="homepage"),
    path('store/', include('store.urls'), name="store"),
]
