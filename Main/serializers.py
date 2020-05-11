from rest_framework import serializers
from .models import Task

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class courseserializers(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


class moduleserializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
