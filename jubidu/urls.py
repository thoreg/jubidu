from django.urls import include
from django.contrib import admin
from django.urls import path

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', index)
]
