from django.contrib import admin
from main.models import teachers
from main.models import lesson
from main.models import course


# Register your models here.
admin.site.register(teachers)
admin.site.register(lesson)
admin.site.register(course)
