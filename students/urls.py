from django.urls import path
from students.views import (StudentList,  
                            StudentDetailView, 
                            StudentEditView, 
                            StudentCreate)
from django.conf.urls import url

urlpatterns = [
    path('students/',StudentList.as_view()),
    path('students/<int:pk>/',StudentDetailView.as_view()),
    path('students/edit/<int:pk>/',StudentEditView.as_view()),
    path('students/create/',StudentCreate.as_view()),
      
]