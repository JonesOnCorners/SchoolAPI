from rest_framework import serializers 
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Courses,  Subjects


class SubjectSerializer(ModelSerializer):    
    class Meta:
        model = Subjects
        fields = '__all__'
        depth = 1
  

class CourseViewSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        depth = 1

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
        
        
                
