from django.urls import path
from department.views import   DepartmentCreateView, DepartmentEditListView

urlpatterns = [
    path('department/create',DepartmentCreateView.as_view()),
    path('department/edit',DepartmentEditListView.as_view()),
    path('department/view/<int:pk>',DepartmentEditListView.as_view()),
    
]