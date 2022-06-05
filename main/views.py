
from cgitb import text
from multiprocessing import context
from winreg import REG_REFRESH_HIVE
from django.shortcuts import render
from main.models import comments, course
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import main.views

# Create your views here.


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context = {
                "username": username,
                "massage": "خوش آمدید "
            }
            return render(request, 'index.html', context)

        else:
            context = {
                "username": username,
                "errorMessage": "کاربری با این مشخصات یافت نشد"
            }
            return render(request, 'login.html', context)
     # Get
    else:
        return render(request, 'login.html', {})

#"logout انجام میشد ولی برای برداشتن نام کاربر از بالای صفحه ارور داشت و فرصت نبود کامنت کردم "
# def logoutView(request):
#     logout(request)
#     context = {
#         "username": " ",
#         "massage": " "
#     }
#     return render(request, 'indext.html', context)


def indexview(request):
    return render(request, 'index.html', context={})


def singupview(request):
    return render(request, 'singup.html', context={})


def coursesview(request):
    courses = course.objects.all()
    context = {
        "courselist": courses

    }
    return render(request, 'courses.html', context)


def coursesinfoview(request, cource_id):
    cours = course.objects.get(pk=cource_id)
    context = {
        "coursedetail": cours
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
    return render(request, 'about.html', context={})


def contactview(request):
    return render(request, 'contact.html', context={})


# def faqview(request):
#     return render(request, 'faq.html', context={})

#مربوط به قسمت نقل قول دوستان در footer
def commentsview(request):

    if request.method == "POST":
        newcomm = comments(
            name=request.post.get('namecomm'),
            email=request.POST('ecomm'),
            text=request.POST('textcomm')
        )
        newcomm.save()
        p = comments.objects.all().order_by('-date')
        context = {
            "comments": p
        }
        return render(request, 'layout.html', context)
