from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('homepage.urls')),
    url(r'', include('cars.urls')),
    url(r'', include('motorbikes.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)