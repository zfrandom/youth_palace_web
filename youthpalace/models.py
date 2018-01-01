from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.
class Student(models.Model):
	GENDER_CHOICES = (
        ('女生', 'Female'),
        ('男生', 'Male'),
    )
	name = models.CharField(max_length=20)
	student_id = models.AutoField(primary_key=True)
	school = models.CharField(max_length=20)
	dateOfBirth = models.DateField(null=True)
	gender = models.CharField(max_length=20, choices = GENDER_CHOICES, null=True)
	active = models.BooleanField(default=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	mom_phone_num = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	dad_phone_num = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	transportation = models.CharField(max_length=20)
	mom_name = models.CharField(max_length=10, blank=True)
	dad_name = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.name

class Teacher(models.Model):
	GENDER_CHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
	name = models.CharField(max_length=20)
	teacher_id = models.AutoField(primary_key = True)
	gender=models.CharField(max_length=6, choices = GENDER_CHOICES, null=True)
	active = models.BooleanField(default=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_num = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	def __str__(self):
		return self.name

class Course(models.Model):
	TERMS = (
		('None',None),
        ('Spring', 'Spring'),
        ('Fall', 'Fall'),
        ('Summer','Summer'),
    )
	name = models.CharField(max_length = 20)
	course_id = models.AutoField(primary_key = True)
	teaching_cost = models.IntegerField(default =0)
	book_cost = models.IntegerField(default = 0)
	cost = models.IntegerField(default = 0)
	def total_cost(self, b, t):
		self.cost = b+t
	room = models.CharField(max_length=10, blank=True)
	active = models.BooleanField(default=True)
	start_date = models.DateField(default=timezone.now)
	end_date = models.DateField(default =timezone.now()+datetime.timedelta(days=90))
	term = models.CharField(max_length=6, choices = TERMS,default='None', null=True, blank=True)
	teacher = models.ForeignKey('youthpalace.Teacher', related_name='course', null=True)
	course_length = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Payment(models.Model):
	student = models.ForeignKey('youthpalace.Student', related_name='payments')
	amount = models.FloatField(default= 0)
	note = models.CharField(max_length=200)
	recorder = models.ForeignKey(settings.AUTH_USER_MODEL, default =1 )
	date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.note
class Student_Course(models.Model):
	student = models.ForeignKey('youthpalace.Student', related_name = 'course')
	course = models.ForeignKey('youthpalace.Course', related_name ='student')
	discount = models.FloatField(default = 10)
	freeBook = models.BooleanField(default=False)
	freeClass = models.BooleanField(default = False)
	cost = models.IntegerField(default = 1, null=True)
	def calculate_cost(self):
		self.cost = (self.course.book_cost*(1-self.freeBook) + (1-self.freeClass)*self.course.teaching_cost*self.discount*0.1)
	def __str__(self):
		return self.student.name +"_"+self.course.name
	


