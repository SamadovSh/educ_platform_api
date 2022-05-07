from django.contrib import admin
from .models import Course, Teacher, Student, CourseStudent

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(CourseStudent)
