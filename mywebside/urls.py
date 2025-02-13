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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from home.views import index
from home.views import contactus
from home.views import about
from home.views import tutor
from home.views import student
from home.views import subjects
from home.views import subject_detail
from django.conf.urls.static import static
from django.utils.safestring import mark_safe
from course import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index, name = 'home'),
    path('',index, name = 'home'),
    path('course/',views.index, name = 'course'),
    path('contact/',contactus, name = 'contact'),
    path('about/',about, name = 'about'),
    path('tutors/',tutor, name = 'tutor'),
    path('student/',student, name = 'student'),
    path('subjects/',subjects, name = 'subjects'),
    path('subject/<int:id>/<slug:slug>',subject_detail, name = "subject_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

