from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def Overview(request):
    urls = {
    'Course': '/course/',
    'Student' : '/student/',
    'Teacher': '/teacher/',
    }
    return Response(urls)

# for courses
@api_view(['GET'])
def CourseOverview(request):

    course_urls = {
    'List': '/course/list/',
    'Detail View' : '/course/detail/<str:pk>',
    'Create' : '/course/create/',
    'Create Module' : 'module/create/',
    'Update' : '/course/update/<str:pk>/',
     'Update Module' : 'module/update/<str:pk1>/<str:pk2>/'

    }
    return Response(course_urls)

#Course lists
@api_view(['GET'])
def courselist(request):
    courses = Course.objects.all().order_by('-id')
    serializer = courseserializers(courses, many=True)
    return Response(serializer.data)

#Particular course details
@api_view(['GET'])
def coursedetails(request,pk):
    courses = Module.objects.all().filter(course_id=pk)

    serializer = moduleserializers(courses, many=True)
    return Response(serializer.data)

#create course
@api_view(['POST'])
def coursecreate(request):
    serializer = courseserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Create module
@api_view(['POST'])
def modulecreate(request):
    serializer = moduleserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#Update Course
@api_view(['PUT'])
def courseupdate(request,pk):
    courses = Course.objects.get(id=pk)
    serializer = courseserializers(instance = courses,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

#Update module in courses
@api_view(['PUT'])
def moduleupdate(request,pk1,pk2):
    modules = Module.objects.get(course_id = pk1,index_number = pk2)
    serializer = moduleserializers(instance = modules,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

#Teacher list
@api_view(['GET'])
def teacherview(request):
    teachers = Teacher.objects.all().order_by('-id')
    serializer = teacherserializers(teachers, many = True)
    return Response(serializer.data)
