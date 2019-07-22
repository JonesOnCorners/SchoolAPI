from rest_framework import serializers 
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Courses, Department, Subjects



class SubjectSerializer(ModelSerializer):    
    class Meta:
        model = Subjects
        fields = ['subject_name','department_name']


class DepartmentSerializer(ModelSerializer):    
    dept_subject_name = SubjectSerializer()
    class Meta:
        model = Department
        fields = ['department_name','dept_subject_name']

class CourseSerializer(ModelSerializer):
#    course_names = serializers.RelatedField(many = True, read_only = True)
    subject = SubjectSerializer(many=True)
    department   = DepartmentSerializer(many = False)
    class Meta:
        model = Courses
        fields = '__all__'