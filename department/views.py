from django.shortcuts import render
from department.serializers import  DepartmentSerializer
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView)
from courses.models import Courses,  Subjects
from department.models import Department


class DepartmentCreateView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentEditListView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

