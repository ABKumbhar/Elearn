from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'course', views.CourseViewSet)
router.register(r'teacher', views.TeacherViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'module', views.ModuleViewSet)
router.register(r'modulefile', views.ModuleFileViewSet)
router.register(r'coursefile', views.CourseFileViewSet)



urlpatterns= [
      path('', include(router.urls)),
      path('front/',views.Test),

      # path('', views.Overview, name="Overview"),
      # path('course/', views.CourseOverview,name = "course"),
      # path('course/list/',views.courselist,name='course-list'),
      # path('course/detail/<str:pk>/',views.coursedetails,name='course-detail'),
      # path('course/create/',views.coursecreate,name='course-create'),
      # path('course/module/create/',views.modulecreate,name='module-create'),
      # path('course/module/update/<str:pk1>/<str:pk2>/',views.moduleupdate,name='module-update'),
      #
      # path('course/update/<str:pk>/',views.courseupdate,name='course-update'),
      # path('student/',views.studentview,name='student'),
      #
      # path('teacher/',views.teacherview,name='teacher-view'),



]
