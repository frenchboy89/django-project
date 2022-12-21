from django.urls import path

from blog.views import index,about,pricing,contact,dashboard,trys

urlpatterns = [
    
    path('',index, name="home"),
    path('about/',about, name="about"),
    path('pricing/',pricing , name= "pricing"),
    path('contact/',contact , name= "contact"),
    path('dashboard/',dashboard, name= "dashboard"),
    path('try/',trys, name= "try"),


    
]
