from django.db import models

# Create your models here.
class teachers(models.Model):       
    name= models.CharField(max_length=200)
    def __str__(self):
     pass




class lesson(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        pass
   





class course(models.Model):
    name= models.CharField(max_length=200)
    date=models.DateField()
    classtime=models.TimeField()
    teacher=models.ManyToManyField(teachers)
    # student=models.ManyToManyField("students",on_delete=CASCADE)
 
    explane=models.TextField(max_length=40000)
    def __str__(self):
        pass




