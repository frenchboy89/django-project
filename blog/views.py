from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Blog, Car

def index(request):
    blogs = Blog.objects.all()
    total = len(blogs)
    return HttpResponse(f"The total number of blog objects in the Blog class is {total}")



def about(request):
    return HttpResponse("Hello,world. You're at the blog about")   
def pricing(request):
    return HttpResponse("Hello,world. You're at the blog pricing")
def contact(request):
    return HttpResponse("Hello,world. You're at the blog contact us")     
def dashboard(request):
    return HttpResponse("Hello,world. You're at the blog dashboard")             



