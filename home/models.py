from django.db import models
# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    smtp_email = models.CharField(max_length=100)
    smtp_password = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    YouTube = models.CharField(max_length=100)
    Instagram = models.CharField(max_length=100)
    Facebook = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/')
    aboutus = models.TextField()
    contact = models.TextField()
    def __str__(self):
        return self.title
