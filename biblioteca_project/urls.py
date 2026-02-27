from django.contrib import admin
from django.urls import path, include
from libros import web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API REST
    path('api/', include('libros.api_urls')),
    
    # OAuth URLs de allauth (para login con Google/Facebook)
    path('accounts/', include('allauth.urls')),
    
    # ← AGREGAR: OAuth 2.0 URLs de django-oauth-toolkit
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('', web_views.home, name='home'),
    path('oauth/login/', web_views.oauth_login, name='oauth_login'),
    path('login/jwt/', web_views.jwt_login_page, name='jwt_login_page'),
]