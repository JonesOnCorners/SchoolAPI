from django.db import models

# Create your models here.

class Department(models.Model):        
    department_name = models.TextField()
    
    def __str__(self):
        return self.department_name
