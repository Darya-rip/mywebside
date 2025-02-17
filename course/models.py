from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img scr="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Student(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Tutor(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
