from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation.trans_real import translation

from home.models import Setting, ContactForm
from course.models import Course
from course.models import Subject
from course.models import Tutor
from course.models import Student
from home.models import ContactMessage
from django.contrib import messages
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
    tutor_cr = Tutor.objects.all().order_by('id')
    setting = Setting.objects.get()
    context = {'tutor_cr':tutor_cr,
               'setting': setting }
    return render(request,'Tutor.html',context)

def subjects(request):
    subjects_cr = Subject.objects.all().order_by('id')
    setting = Setting.objects.get()
    context = {'subjects_cr':subjects_cr,
               'setting': setting }
    return render(request,'subjects.html',context)

def student(request):
    student_cr = Student.objects.all().order_by('id')
    setting = Setting.objects.get()
    context = {'student_cr':student_cr,
               'setting': setting }
    return render(request,'students.html',context)

def subject_detail(request, id, slug):
    subject_cr = Subject.objects.all().order_by('id')[:4]
    setting = Setting.objects.get()
    subject = Subject.objects.get(pk=id)
    course = Course.objects.all()
    context = {'student_cr': subject_cr,
               'setting': setting,
               'subject': subject,
               'course':course }
    return render(request, 'subject_detail.html', context)

def contactus(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'contact.html',context)

def about(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'aboutus.html',context)

def contact(request):
    if request.metod == 'POST':
        form = ContactMessage()
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Thanks, '+data.name +'we received your message and will respond shortly...')
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.get()
    form = ContactForm
    context = { 'setting':setting }
    return render(request,'contact.html',context)

def selectlanguage(request):
    if request.metod == 'POST':
        lang = request.POST['language']
        translation.activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME]= lang
        return HttpResponseRedirect('/'+ lang )
