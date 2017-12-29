from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.student_list, name='student_list'),
    url(r'^teacher/$', views.teacher_list, name='teacher_list'),
    url(r'^course/$', views.course_list, name='course_list'),
    #url(r'^staff/$', views.staff_list, name='staff_list'),
    url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^teacher/(?P<pk>\d+)/$', views.teacher_detail, name='teacher_detail'),
    url(r'^course/(?P<pk>\d+)/$', views.course_detail, name='course_detail'),
    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^course/new/$', views.course_new, name='course_new'),
    url(r'^teacher/new/$', views.teacher_new, name='teacher_new'),
    url(r'^student/(?P<pk>\d+)/drop_course/$', views.student_drop_course, name ='student_drop_course'),
    url(r'^student/(?P<pk>\d+)/add_payment/$', views.payment_new, name ='payment_new'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
    url(r'^student/(?P<pk>\d+)/add_course/$', views.student_add_course, name ='student_add_course'),
    url(r'^teacher/(?P<pk>\d+)/edit/$', views.teacher_edit, name='teacher_edit'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
]
