from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from students.models import Student
from students.serializers import StudentSerializer, StudentDisplaySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser 

# Create your views here.

 #View to handle student creation          
class StudentCreate(generics.CreateAPIView):
    permission_classes  = [ IsAdminUser ]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#View that handles displaying entire student list
class StudentList(generics.ListAPIView):
    permission_classes  = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentDisplaySerializer

#View that handles displaying details of a single student  
class StudentDetailView(generics.RetrieveAPIView):    
    permission_classes  = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentDisplaySerializer        

#View to handle put request for individual student
class StudentEditView(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes  = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer        


   
