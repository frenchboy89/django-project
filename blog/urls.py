from django.urls import path


from blog import views

urlpatterns = [
    
    path('',views.index, name="home"),
    path('books/',views.book_list, name="books"),
    path('pricing/',views.pricing , name= "pricing"),
    path('contact/',views.contact , name= "contact"),
    path('dashboard/',views.dashboard, name= "dashboard"),
    path('try/',views.trys, name= "try"),
    path('blog-details/<pk>/',views.blog_details, name="blog_details"),
    path('book-details/<pk>/',views.book_details, name="book_details"),
    




    
]
