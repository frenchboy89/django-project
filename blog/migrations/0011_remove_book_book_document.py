# Generated by Django 4.1.3 on 2023-01-23 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blog_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_document',
        ),
    ]