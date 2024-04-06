from django.db import models


class Position(models.Model):
    title =  models.CharField(max_length=60)

    def  __str__(self):
        return self.title
    

class Employee(models.Model):
    fullname = models.CharField(max_length=220)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=13)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fullname
    

# Create your models here.
