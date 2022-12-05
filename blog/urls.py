from django.urls import path

from blog.views import index,about,pricing,contact,dashboard

urlpatterns = [
    
    path('index/',index),
    path('about/',about),
    path('pricing/',pricing),
    path('contact/',contact),
    path('dashboard/',dashboard)    ,

    
]
