# from unicodedata import name
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class teachers(models.Model):
    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "استاد"
    name = models.CharField(max_length=200, verbose_name="نام")

    def __str__(self):
        return self.name

class course(models.Model):
    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره"

    name = models.CharField(max_length=200, verbose_name="نام")
    startdatetime = models.DateTimeField(
        blank=True, null=True, verbose_name="زمان شروع دوره")
    timeperiod = models.IntegerField(
        verbose_name="مدت آموزش (ساعت)", null=True)
    teacher = models.ForeignKey(teachers, verbose_name=(
        "استاد"), on_delete=models.CASCADE, null=True)
    poster = models.ImageField(
        upload_to="courseimage/", null=True, verbose_name="پوستر")

    explane = models.TextField(max_length=40000)

    def __str__(self):
        return f"name:{self.name} ,timeperiod:{self.timeperiod},teacher:{self.teacher}, explane:{self.explane}"


class comments(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    text=models.TextField(max_length=5000)

    def __str__(self):
        return f"name:{self.name} , text:{self.text}"



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

