from django.utils import timezone
from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Blog, Car, Book, Category

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

def blog_details(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        "blog":blog
    }

    return render(request,'blog_details.html',context)


def book_list(request):
    books =Book.objects.all()
    total = len(books)
    categories = Category.objects.all

    context = {
        "books": books,
        "average": total,
        "categories": categories,
    }
    
    return render(request, "books.html",context)

def book_details(request, pk):
    book = Book.objects.get(id=pk)
    pdf = book.material.url
    context = {
        "book":book, 
        "pdf" :pdf,
    }

    return render(request,'book_details.html',context)
    
def category_list(request, slug):
  category = Category.objects.get(slug=slug)
  books = Book.objects.filter(category=category)
  context = {
    'books': books,
    'category': category,
  }
  return render(request, 'category_list.html', context)





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

def trys(request):
    return render(request, "try.html")  




