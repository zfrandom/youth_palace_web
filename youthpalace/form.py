from django import forms
from .models import Teacher, Student, Course, Student_Course, Payment
from django.utils.translation import gettext_lazy as _
class StudentForm(forms.ModelForm):
	class Meta: #which model should be used to create this form
		model = Student
		fields = ('name','school','dateOfBirth','gender','mom_name', 'dad_name', 'mom_phone_num','dad_phone_num','transportation',) #which field should end up in our form
		labels = {
			'name':_('学生姓名'),
			'dateOfBirth':_('生日'),
			'school':_('就读学校'),
			'gender':_('性别'),
			'mom_name':_('母亲姓名'),
			'dad_name':_('父亲姓名'),
			'mom_phone_num':_('母亲电话'),
			'dad_phone_num':_('父亲电话'),
			'transportation':_('放学回家交通'),
		}
class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ('name','phone_num','gender')

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields=('name', 'book_cost','teaching_cost','teacher','room','term','start_date','end_date','course_length')
		labels ={
			'book_cost':_('书本费／其它费用'),
			'teaching_cost':_('教学费'),
			'course_length':_('每节课时长')
		}

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields=('amount', 'note',)
		labels={
			'amount':_('金额'),
			'note':_('备注'),
			}
		help_texts ={
			'note':_('备注填写付费课程')
		}

		

class Student_CourseForm(forms.ModelForm):
	class Meta:
		model = Student_Course
		fields=('course',)



