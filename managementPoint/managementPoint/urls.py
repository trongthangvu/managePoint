from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('point/', include('point.urls')),
    path('admin/', admin.site.urls),  # Thay đổi tên không gian URL của admin
    path('o/', include('oauth2_provider.urls', namespace='oauth2')),  # Thay đổi tên không gian URL của oauth2_provider
]
