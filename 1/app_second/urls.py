from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from . import views

urlpatterns = [

    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
]

# urlpatterns += [re_path(r'^.*$', lambda request: redirect('', permanent=False), name='redirect')]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
