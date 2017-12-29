from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student, Course, Student_Course, Payment
from .form import StudentForm, TeacherForm, CourseForm, PaymentForm, Student_CourseForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
def index(request):
	return render(request, 'youthpalace/base.html')
@login_required
def student_list(request):
	students = Student.objects.all()
	return render(request, 'youthpalace/student_list.html', {'students': students})

def course_list(request):
	courses = Course.objects.all()
	return render(request, 'youthpalace/course_list.html', {'courses': courses})
@login_required
def teacher_list(request):
	teachers = Teacher.objects.all()
	return render(request, 'youthpalace/teacher_list.html', {'teachers': teachers})
@login_required
def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	student_course = student.course.all()
	courses = Course.objects.all()
	return render(request, 'youthpalace/student_detail.html', {'student': student, 'courses':courses})
@login_required
def teacher_detail(request, pk):
	teacher = get_object_or_404(Teacher, pk=pk)
	return render(request, 'youthpalace/teacher_detail.html', {'teacher': teacher})

def course_detail(request, pk):
	course = get_object_or_404(Course, pk=pk)
	return render(request, 'youthpalace/course_detail.html', {'course': course})
@login_required
def student_new(request):
	if request.method=="POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.save()
			return redirect('student_detail', pk=student.pk)
	else:
		form = StudentForm()
	return render(request, 'youthpalace/student_edit.html', {'form':form})
@permission_required('youthpalace.course.can_add_course')
def course_new(request):
	if request.method=="POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			course.save()
			return redirect('course_detail', pk=course.pk)
	else:
		form = CourseForm()
	return render(request, 'youthpalace/student_edit.html', {'form':form})
@login_required	
def student_edit(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
		form = StudentForm(request.POST, instance =student)
		if form.is_valid():
			student = form.save(commit=False)
			#post.published_date = timezone.now()
			student.save()
			return redirect('student_detail', pk=student.pk)
	else:
		form = StudentForm(instance = student)
	return render(request, 'youthpalace/student_edit.html', {'form': form})
@permission_required('youthpalace.teacher.can_edit_teacher')
def teacher_edit(request, pk):
	teacher = get_object_or_404(Teacher, pk=pk)
	if request.method == "POST":
		form = TeacherForm(request.POST, instance =teacher)
		if form.is_valid():
			teacher = form.save(commit=False)
			#post.published_date = timezone.now()
			teacher.save()
			return redirect('teacher_detail', pk=teacher.pk)
	else:
		form = TeacherForm(instance = teacher)
	return render(request, 'youthpalace/student_edit.html', {'form': form})
@permission_required('youthpalace.course.can_edit_course')
def course_edit(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.method == "POST":
		form = CourseForm(request.POST, instance =course)
		if form.is_valid():
			course = form.save(commit=False)
			#post.published_date = timezone.now()
			course.save()
			return redirect('course_detail', pk=course.pk)
	else:
		form = CourseForm(instance = course)
	return render(request, 'youthpalace/student_edit.html', {'form': form})
@login_required
def student_drop_course(request, pk):
	student_course = get_object_or_404(Student_Course, pk=pk)
	student_course.delete()
	return redirect('student_detail', pk=student_course.student.pk)
# Create your views here.
@login_required
def payment_new(request, pk):
	if request.method=="POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			payment = form.save(commit=False)
			payment.date = timezone.now()
			payment.student = get_object_or_404(Student, pk=pk)
			payment.recorder = request.user
			payment.save()
			return redirect('student_detail', pk=pk)
	else:
		form = PaymentForm()
	return render(request, 'youthpalace/payment_new.html', {'form':form})
@login_required
def teacher_new(request):
	if request.method=="POST":
		form = TeacherForm(request.POST)
		if form.is_valid():
			teacher = form.save(commit=False)
			teacher.save()
			return redirect('teacher_detail', pk=teacher.teacher_id)
	else:
		form = TeacherForm()
	return render(request, 'youthpalace/student_edit.html', {'form':form})
@login_required
def student_add_course(request, pk):
	student=get_object_or_404(Student, pk=pk)
	if request.method=="POST":
		print(request.POST.getlist('choice'))
		for c in request.POST.getlist('choice'):
			cou = get_object_or_404(Course, pk=c)
			sc = Student_Course(student = student, course=cou)
			sc.save()
		return redirect('student_detail', pk=pk)
	else:
		selected = student.course.all().values('course_id')
		select = Course.objects.exclude(course_id__in=selected)
		print(select)
		#form = Student_CourseForm()
	return render(request, 'youthpalace/student_add_course.html',{'courses':select})

