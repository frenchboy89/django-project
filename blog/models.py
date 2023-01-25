from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to="blog_img", blank=True )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Car(models.Model):
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    description = models.TextField()
    engine = models.IntegerField()
    numbers_of_tier = models.IntegerField()
    material = models.CharField(max_length=30)
    created_on = models.DateTimeField()
    number_of_sit = models.IntegerField()

    def __str__(self) -> str:
        return self.model_name


class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, blank=True)
  
  def __str__(self) -> str:
    return f'{self.name}'

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    return super().save(self, *args, **kwargs)


class Book(models.Model):
    ATTR = (
        ("BEST SELLING", "BEST SELLING"),
        ("TOP 100", "TOP 100"),
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    excerpt = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    publication_date = models.DateField()
    attribute = models.CharField(max_length=100, choices=ATTR, blank=True)
    image = models.ImageField( blank=True, upload_to="book_img")
    is_trending = models.BooleanField(True) 
    num_pages = models.IntegerField()
    material = models.FileField(blank=True, upload_to="book_docs" )
    isbn_number = models.PositiveIntegerField()
   
    def __str__(self) -> str:
        return self.title
