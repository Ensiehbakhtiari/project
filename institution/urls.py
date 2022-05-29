"""institution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', main.views.indexview),
    path('singup/', main.views.singupview),
    path('courses/',main.views.coursesview), 
    path('coursesinfo/',main.views.coursesinfoview), 
    path('meetings/',main.views.meetingsview), 
    path('blog/',main.views.blogview), 
    path('news/',main.views.newsview), 
    path('single/',main.views.singleview), 
    path('gallerycat/',main.views.gallerycatview), 
    path('gallery/',main.views.galleryview), 
    path('about/',main.views.aboutview), 
    path('contact/',main.views.contactview), 
    path('faq/',main.views.faqview), 

]
