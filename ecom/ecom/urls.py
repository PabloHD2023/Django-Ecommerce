from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Include the store app URLs
    path('cart/', include('cart.urls')),  # Include the cart app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
