"""
URL configuration for football_transfers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from asosiy.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('clubs/', clubs),
    path('players/', players),
    path('tryouts/', tryouts),
    path('latest_transfers/', latest_transfers),
    path('u_20players/', u20_players),
    path('stats/', stats),
    path('about/', about),
    path('transfer_records/', transfer_records),
    path('transfer_archive/', transfer_archive),
    path('transfers/<str:season>/', season_transfers),
    path('players/<int:pk>/', club_players),
    path('clubs/<str:name>/', country_clubs)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
