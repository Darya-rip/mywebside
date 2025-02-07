"""
URL configuration for mywebside project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import index
from home.views import index1
from home.views import index2
from home.views import tutor
from course import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index, name = 'home'),
    path('',index, name = 'home'),
    path('course/',views.index, name = 'course'),
    path('contact/',index1, name = 'contact'),
    path('about/',index2, name = 'about'),
    path('tutors/',tutor, name = 'tutor'),
]
