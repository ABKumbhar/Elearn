from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskserializers
from .models import Task
# Create your views here.

# for courses
@api_view(['GET'])
def apiOverview(request):

    course_urls = {
    'List': '/course-list',
    'Detail View' : '/course-detail/<str:pk>',
    'Create' : '/course-create/',
    'Update' : '/course-update/<str:pk>',
    }
    return Response(task_urls)


@api_view(['GET'])
def tasklist(request):
    course = Course.objects.all().order_by('-id')
    serializer = taskserializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetails(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = taskserializers(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = taskserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = taskserializers(instance = tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Item succefully deleted')
