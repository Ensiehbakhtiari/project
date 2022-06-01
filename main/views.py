from multiprocessing import context
from django.shortcuts import render
from main.models import course
# Create your views here.


def indexview(request):
    return render(request, 'index.html', context={})


def singupview(request):
    return render(request, 'singup.html', context={})

def coursesview(request):
    courses=course.objects.all()
    context={ 
        "courselist":courses
  
    }
    return render(request, 'courses.html', context)


def coursesinfoview(request,cource_id):
    cours=course.objects.get(pk=cource_id)
    context={ 
         "coursedetail":cours
         }

    return render(request, 'courses-info.html', context)
    
def meetingsview(request):
    return render(request, 'meetings.html', context={})

def blogview(request):
    return render(request, 'blog.html', context={})

def newsview(request):
    return render(request, 'news.html', context={})

def singleview(request):
    return render(request, 'single.html', context={})

def gallerycatview(request):
    return render(request, 'gallery-cat.html', context={})

def galleryview(request):
    return render(request, 'gallery.html', context={})

def aboutview(request):
    return render(request,'about.html',context={})

def contactview(request):
    return render(request,'contact.html',context={})
    
def faqview(request):
    return render(request,'faq.html',context={})    

