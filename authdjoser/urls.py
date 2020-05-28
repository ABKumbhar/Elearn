from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views




urlpatterns = [
    path('', include('djoser.urls')),

    path('', include('djoser.urls.authtoken')),
    


 ]
