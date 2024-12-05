"""
URL configuration for bloggerweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve
from . import views  # Importing the views from the current directory (the same directory as this urls.py)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),  # Assuming you have a 'tweet' app
    path('accounts/', include('django.contrib.auth.urls')),  # Accounts URLs for login, logout, etc.
    path('', views.home, name='home'),  # Home page at the root
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),# for root link 
]

# Serve media files during development
if settings.DEBUG:  # Only add this during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
