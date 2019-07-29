from django.db import models
from courses.models import Courses

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 200, blank = False, default = "")
    middle_name= models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200, blank = False, default = "")
    address   = models.TextField(blank = False, default ="")
    email  =  models.EmailField(default = "")
    course = models.ForeignKey(Courses, 
             default = 1,
             on_delete = models.CASCADE,
             related_name = 'student_course'
             )

