from django.shortcuts import render
from Main.models import *
# Create your views here.
from authdjoser.models import User
from rest_framework import generics
from rest_framework import viewsets

from authdjoser.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from djoser.views import *
from djoser.compat import get_user_email
from djoser.conf import settings



    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        if (self.request.user.Typeofuser) == 'S':
            Student.objects.create(user = self.request.user, name = self.request.user.first_name)
        
        else :
            Teacher.objects.create(user = self.request.user, name = self.request.user.first_name)

    
    def perform_update(self, serializer):
        instance = serializer.save()
        send_email_confirmation(user=self.request.user, modified=instance)
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    




