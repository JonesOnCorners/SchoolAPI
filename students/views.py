from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

           
class StudentCreate(generics.CreateAPIView):
    permission_classes  = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentList(generics.ListAPIView):
    permission_classes  = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  
class StudentDetailView(generics.RetrieveAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer        

class StudentEditView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer        


   
