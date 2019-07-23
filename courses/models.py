from django.db import models




class Subjects(models.Model):
    subject_name = models.TextField()

    def __str__(self):
        return self.subject_name

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
    



    





