from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
from Main.models import *
from Main.serializers import *
from django.db import models
from django.contrib.auth.models import Group


class UserSerializer(UserSerializer):
    student = studentserializers()
    teacher = teacherserializers()
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','Typeofuser','student','teacher')
    
 

    def create(self, validated_data):
        
        user = User.objects.create(**validated_data)
        

        
        if (user.Typeofuser == 'S') :
            group = Group.objects.get(name='Student')
            user.groups.add(group)

            stu = Student(user=user)
            stu.save()

        

        else :
            group = Group.objects.get(name='Teacher')
            user.groups.add(group)

            tea = Teacher(user=user)
            tea.save()

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
