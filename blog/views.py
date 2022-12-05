from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")
def about(request):
    return HttpResponse("Hello,world. You're at the blog about")   
def pricing(request):
    return HttpResponse("Hello,world. You're at the blog pricing")
def contact(request):
    return HttpResponse("Hello,world. You're at the blog contact us")     
def dashboard(request):
    return HttpResponse("Hello,world. You're at the blog dashboard")             



