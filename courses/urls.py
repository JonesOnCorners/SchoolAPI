from django.urls import path
from courses.views import CourseCreateView, CourseDestroyView,CourseListView,   SubjectView

urlpatterns = [
    path('course/create',CourseCreateView.as_view()),
    path('course/view',CourseListView.as_view()),
    path('course/view/<int:pk>',CourseListView.as_view()),
    path('course/delete/<int:pk>',CourseDestroyView.as_view()),
    path('subject/create',SubjectView.as_view()),
]