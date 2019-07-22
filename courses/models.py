from django.db import models


# Create your models here.
class Department(models.Model):        
    department_name = models.TextField()
    def __str__(self):
        return self.department_name

class Subjects(models.Model):
    subject_name = models.TextField()

class Courses(models.Model):
    course_name = models.TextField()
    course_departments = models.ForeignKey(
             'Department',
             default = 1,
             on_delete = models.CASCADE,
             related_name  = 'course_names'
     )
    course_credits = models.IntegerField(default = '10')
    subjects = models.ManyToManyField(Subjects)
    



    





