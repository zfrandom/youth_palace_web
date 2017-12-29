from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	student_id = models.AutoField(primary_key=True)
	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=20)
	teacher_id = models.AutoField(primary_key = True)
	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length = 20)
	course_id = models.AutoField(primary_key = True)
	cost = models.IntegerField(default =0)
	teacher = models.ForeignKey('youthpalace.Teacher', related_name='course', null=True)
	def __str__(self):
		return self.name

class Payment(models.Model):
	student = models.ForeignKey('youthpalace.Student', related_name='payments')
	amount = models.IntegerField(default= 0)
	note = models.CharField(max_length=200)
	recorder = models.ForeignKey(settings.AUTH_USER_MODEL, default =1 )
	date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.note
class Student_Course(models.Model):
	student = models.ForeignKey('youthpalace.Student', related_name = 'course')
	course = models.ForeignKey('youthpalace.Course', related_name ='student')


