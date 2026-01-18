from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')), # dołączamy reguły url z pliku posts\urls.py
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('posts.api_urls')),
] + debug_toolbar_urls()
