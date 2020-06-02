from rest_framework import serializers
from .models import *



class modulefileserializers(serializers.ModelSerializer):
    class Meta:
        model = ModuleFile
        fields = '__all__'

class coursefileserializers(serializers.ModelSerializer):
    class Meta:
        model = CourseFile
        fields = '__all__'

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class moduleserializers(serializers.ModelSerializer):
    # modulefile = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='modulefile-detail'
    #     )
    modulefile = modulefileserializers(many=True, read_only=True)

    class Meta:
        model = Module
        fields = '__all__'

class courseserializers(serializers.ModelSerializer):
    # modules = serializers.HyperlinkedRelatedField(
    # many=True,
    # read_only=True,
    # view_name='module-detail'
    # )
    modules = moduleserializers(many=True,read_only=True)
    # coursefile = serializers.HyperlinkedRelatedField(
    # many=True,
    # read_only=True,
    # view_name='coursefile-detail'
    # )
    coursefile = coursefileserializers(many=True,read_only=True)
    class Meta:
        model = Course
        fields = '__all__'




class teacherserializers(serializers.ModelSerializer):
    # courses = serializers.HyperlinkedRelatedField(
    # many=True,
    # read_only=True,
    # view_name='course-detail'
    # )
    courses = courseserializers(read_only=True,many=True)
    class Meta:
        model = Teacher
        fields = '__all__'

