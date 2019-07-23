from rest_framework import serializers 
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Courses,  Subjects


class SubjectSerializer(ModelSerializer):    
    class Meta:
        model = Subjects
        fields = '__all__'
  

class CourseViewSerializer(ModelSerializer):
#    course_names = serializers.RelatedField(many = True, read_only = True)
    # subjects = serializers.SerializerMethodField('get_subject_name')

    # def get_subject_name(self, obj):
    #     return self.subjects.subject_name
    #subjects = serializers.RelatedField(many = True, read_only = True)
    #subjects = SubjectSerializer()
    class Meta:
        model = Courses
        fields = '__all__'
        depth = 1

class CourseSerializer(ModelSerializer):
#    course_names = serializers.RelatedField(many = True, read_only = True)
    # subjects = serializers.SerializerMethodField('get_subject_name')

    # def get_subject_name(self, obj):
    #     return self.subjects.subject_name
    #subjects = serializers.RelatedField(many = True, read_only = True)
    #subjects = SubjectSerializer()
    class Meta:
        model = Courses
        fields = '__all__'
        
                
        


