from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting
from course.models import Course
from course.models import Subject
from course.models import Tutor

# Create your views here.

def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page = 'home'
    context = {'setting':setting,
               'page' : page,
               'course_cr' : course_cr,
               'subject_cr': subject_cr,
               'course': course,
               'tutor_cr':tutor_cr,
    }
    return render(request, "index.html", context)

def tutor(request):
    tutor_cr = Tutor.objects.all()
    context = {'tutor_cr':tutor_cr}
    return render(request,'Tutor.html',context)

def index1(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'contact.html',context)

def index2(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'aboutus.html',context)

