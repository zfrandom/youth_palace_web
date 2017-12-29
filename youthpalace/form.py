from django import forms
from .models import Teacher, Student, Course, Student_Course, Payment

class StudentForm(forms.ModelForm):
	class Meta: #which model should be used to create this form
		model = Student
		fields = ('name',) #which field should end up in our form

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ('name',)

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields=('name', 'cost','teacher',)

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields=('amount', 'note',)

class Student_CourseForm(forms.ModelForm):
	class Meta:
		model = Student_Course
		fields=('course',)



