from django.urls import path
from students.views import StudentList,  StudentDetailView
from django.conf.urls import url

urlpatterns = [
    path(r'students/',StudentList.as_view(), name = "list-view"),
    path(r'students/<int:pk>/',StudentDetailView.as_view(), name = "detail-view"),
      
]