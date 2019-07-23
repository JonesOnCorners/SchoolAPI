from django.shortcuts import render
from .serializers import CourseSerializer,  SubjectSerializer, CourseViewSerializer
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView)
from courses.models import Courses,  Subjects

# Create your views here.

class CourseCreateView(CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class CourseListView(RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseViewSerializer

class CourseDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseViewSerializer


class SubjectView(CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer