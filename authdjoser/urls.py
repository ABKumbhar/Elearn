from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [

    path('', include('djoser.urls')),
    
    path('', include('djoser.urls.authtoken')),
    


 ]
