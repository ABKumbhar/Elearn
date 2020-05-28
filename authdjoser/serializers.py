from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
from Main.models import *
from Main.serializers import *
from django.db import models
from django.contrib.auth.models import Group

class UserSerializer(UserSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','Type_of_user')

    def create(self, validated_data):
        
        user = User.objects.create(**validated_data)
        
        group = Group.objects.get(name='Student')
        user.groups.add(group)
        
        if user.objects.get(Type_of_user='S') :


            student = Student(user=user, name=user.first_name)
            student.save()

        

        else :
            group = Group.objects.get(name='Teacher')
            user.groups.add(group)

            teacher = Teacher(user=user, name=user.first_name)
            teacher.save()
            
        return user    

        

# class UserManager(models.Manager):
    
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id','email','username','password','first_name','last_name','Type_of_user')

#     ...

#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
        
#         profile = Student(
#             user=user,
#             is_premium_member=is_premium_member,
#             has_support_contract=has_support_contract
#         )
#         profile.save()
#         return user
