from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField()

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
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    publication_date = models.DateField()
    image = models.ImageField( blank=True)
    is_trending = models.BooleanField(True) 
    num_pages = models.IntegerField()
    material = models.CharField(max_length=30)
    isbn_number = models.PositiveIntegerField()
    book_document = models.FileField( blank=True)

    def __str__(self) -> str:
        return self.title


 

























