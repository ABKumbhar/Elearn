from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns= [
      path('', views.Overview, name='Overview'),
      path('course/', views.CourseOverview,name = 'course'),
      path('course/list/',views.courselist,name='course-list'),
      path('course/detail/<str:pk>/',views.coursedetails,name='course-detail'),
      path('course/create/',views.coursecreate,name='course-create'),
      path('course/update/<str:pk>/',views.courseupdate,name='course-update'),



]
