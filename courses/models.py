from django.db import models


# Create your models here.
class Department(models.Model):        
    department_name = models.TextField()   
    dept_subject_name = models.ForeignKey('Subjects',
                                     on_delete = models.CASCADE,
                                     default = 1,
                                     related_name = 'dept_subject_name')

class Subjects(models.Model):
    subject_name = models.TextField()
    department_name = models.ForeignKey('Department',
                                 on_delete =  models.CASCADE,
                                 default = 1,
                                 related_name = 'subject_name'
                                )

class Courses(models.Model):
    course_name = models.TextField()
    department = models.ForeignKey(
             'Department',
             default = 1,
             on_delete = models.CASCADE,
             related_name  = 'dept_names'
     )
    course_credits = models.IntegerField(default = '10')
    subject = models.ForeignKey('Subjects',
                                 on_delete =  models.CASCADE,
                                 default = 1,
                                 related_name = 'subjects_course_name'
                                )

    



    





