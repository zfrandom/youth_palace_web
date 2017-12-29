from django.contrib import admin
from .models import Student, Teacher, Payment, Student_Course, Course
# Register your models here.
admin.site.register(Student)
admin.site.register(Student_Course)
admin.site.register(Teacher)
admin.site.register(Payment)
admin.site.register(Course)