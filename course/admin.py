from django.contrib import admin
from course.models import Course
from course.models import Subject
from course.models import Student
from course.models import Tutor
# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ["title", "slug"]
#     list_filter = ['course']
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["name", "description"]
# class TutorAdmin(admin.ModelAdmin):
#     list_display = ["name", "description"]
#     list_filter = ['subject']

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Tutor)