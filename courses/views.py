from django.shortcuts import render
from .serializers import CourseSerializer, DepartmentSerializer, SubjectSerializer
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView)
from courses.models import Courses, Department, Subjects

# Create your views here.

class CourseCreateView(CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class CourseListView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class CourseDestroyView(DestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class DepartmentCreateView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentEditListView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SubjectView(CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer