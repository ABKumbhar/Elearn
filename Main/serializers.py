from rest_framework import serializers
from .models import *




class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class teacherserializers(serializers.ModelSerializer):
    courses = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='course-detail'
    )
    class Meta:
        model = Teacher
        fields = '__all__'

class courseserializers(serializers.ModelSerializer):
    modules = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='module-detail'
    )

    class Meta:
        model = Course
        fields = '__all__'


class moduleserializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
