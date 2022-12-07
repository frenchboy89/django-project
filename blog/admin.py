from django.contrib import admin

from blog.models import Blog,  Car , Book


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
