from argparse import ONE_OR_MORE
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


class news(models.Model):
   from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class news(models.Model):

    STATUS_CHOICES =('draft', 'Draft'),('published', 'Published')


    title = models.CharField(max_length=450)
    slug = models.SlugField(max_length=350,unique_for_date='publish')

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='main_news')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title





class course(models.Model):
    name= models.CharField(max_length=200)
    date=models.DateField()
    classtime=models.TimeField()
    teacher=models.ManyToManyField(teachers)
    # student=models.ManyToManyField("students",on_delete=CASCADE)
 
    explane=models.TextField(max_length=40000)
    def __str__(self):
        pass




