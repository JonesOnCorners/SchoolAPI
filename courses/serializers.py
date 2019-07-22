from rest_framework import serializers 
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Courses, Department, Subjects


class CourseSerializer(ModelSerializer):
#    course_names = serializers.RelatedField(many = True, read_only = True)
    class Meta:
        model = Courses
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    
    class Meta:
        model = Department
        fields = '__all__'

class SubjectSerializer(ModelSerializer):    
    class Meta:
        model = Subjects
        fields = '__all__'