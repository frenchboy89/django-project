from django.utils import timezone
from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Blog, Car, Book

def index(request):
    blogs = Blog.objects.all()
    total = len(blogs)
    now = timezone.now()
    number = 2+2
    context = {
        "blogs": blogs,
        "average": total,
        "now":now,
        "number": number,
    }
    return render(request, 'index.html',context) 



def about(request):
    books =Book.objects.all()
    total = len(books)
    now = timezone.now()
    number = 2+6
    context = {
        "books": books,
        "average": total,
        "now":now,
        "number": number,
    }
    
    return render(request, "about.html",context)

def pricing(request):
    cars = Car.objects.all()


    context = {
        "cars": cars,
         
    }

    return render(request, "pricing.html",context)

def contact(request):
    return render(request, "contact.html" )

def dashboard(request):
    return render(request, "dashboard.html")             



