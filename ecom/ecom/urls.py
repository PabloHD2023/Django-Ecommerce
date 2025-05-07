from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
# This is the main URL configuration for the Django project.
# It includes the admin URLs and the URLs from the store app.
# The `urlpatterns` list routes URLs to views. For more information, see:
# https://docs.djangoproject.com/en/5.2/topics/http/urls/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Include the store app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# The `static()` function is used to serve media files during development.
# In production, you would typically use a web server like Nginx or Apache to serve these files.
