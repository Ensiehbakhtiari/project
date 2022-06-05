from django.contrib import admin
from main.models import teachers
from main.models import course
from main.models import news


# Register your models here.
admin.site.register(teachers)
admin.site.register(course)
admin.site.register(news)
