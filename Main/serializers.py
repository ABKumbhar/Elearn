from rest_framework import serializers
from .models import *




class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class teacherserializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class courseserializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class moduleserializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
