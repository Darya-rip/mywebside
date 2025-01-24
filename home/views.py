from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "index.html")

def index1(request):
    return HttpResponse('Contact page')

def index2(request):
    return HttpResponse('About us')
