from django.contrib import admin
from course.models import Course
from course.models import Subject
# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ["title", "slug"]
#     list_filter = ['course']

admin.site.register(Course)
admin.site.register(Subject)