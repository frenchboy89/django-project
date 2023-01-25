from django.contrib import admin

from blog.models import Blog,  Car , Book ,Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  ...
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

