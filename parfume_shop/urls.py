from django.contrib import admin
from django.urls import path, include

from parfume_shop.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/v1/', include('cart.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls
