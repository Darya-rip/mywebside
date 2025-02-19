from django.contrib import admin
from course.models import Course
from course.models import Subject
from course.models import Student
from course.models import Tutor
from course.models import TutorLang
from course.models import StudentLang
from course.models import CourseLang
from course.models import SubjectLang


# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ["title", "slug"]
#     list_filter = ['course']
class  SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','course','image_tag']
    list_filter = ['course']
    readonly_fields = ('image_tag',)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["name", "description"]
# class TutorAdmin(admin.ModelAdmin):
#     list_display = ["name", "description"]
#     list_filter = ['subject']

admin.site.register(Course)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(TutorLang)
admin.site.register(StudentLang)
admin.site.register(CourseLang)
admin.site.register(SubjectLang)
