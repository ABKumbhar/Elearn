from django.shortcuts import render
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
    'Update' : '/course/update/<str:pk>/',
    }
    return Response(course_urls)


@api_view(['GET'])
def courselist(request):
    courses = Course.objects.all().order_by('-id')
    serializer = courseserializers(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def coursedetails(request,pk):
    courses = Module.objects.all().filter(course_id=pk)

    serializer = moduleserializers(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def coursecreate(request):
    serializer = courseserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def courseupdate(request,pk):
    courses = Course.objects.get(id=pk)
    serializer = courseserializers(instance = courses,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
