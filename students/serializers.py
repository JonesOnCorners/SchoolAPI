from rest_framework.serializers import ModelSerializer
from students.models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','middle_name','last_name','address','email']
        #fields = '__all__'