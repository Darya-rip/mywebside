from django.db import models
from django.forms import TextInput
from django.forms import ModelForm

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=5)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

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

class ContactMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=20, default='New')
    ip = models.CharField(max_length=20)
    note = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','phone','subject','message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'massage': TextInput(attrs={'class': 'input', 'placeholder': 'Your Message','rows':'5'}),
        }
