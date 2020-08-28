from django.db import models

from ckeditor.fields import RichTextField

class Post(models.Model):
    name = models.CharField(max_length=80)
    date = models.DateTimeField()
    text = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True)