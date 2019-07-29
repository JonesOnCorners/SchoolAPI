from rest_framework import serializers 
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from courses.models import Courses,  Subjects
from department.models import Department




class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        #fields = ['department_name']
        depth = 1
