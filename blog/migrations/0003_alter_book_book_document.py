# Generated by Django 4.1.3 on 2022-12-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_document',
            field=models.FileField(upload_to=''),
        ),
    ]
