# Generated by Django 4.1.3 on 2022-12-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_updated_on_alter_blog_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='excerpt',
            field=models.TextField(default='example'),
            preserve_default=False,
        ),
    ]