"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import HomeView
# from .views import home


urlpatterns = [


    # Superuser
    path('admin/', admin.site.urls),

    # Home
    path('', HomeView.as_view(), name='home'),

    # App1 (custom_users)
    # path('', include('custom_users.urls', namespace='custom_users')),

    # App2 (diagnostic_centers)
    # path('', include('diagnostic_centers.urls', namespace='diagnostic_centers')),

    # App3 (tests)
    path('', include('django.contrib.auth.urls'), name='login'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

