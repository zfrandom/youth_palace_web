# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 17:59
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('teaching_cost', models.IntegerField(default=0)),
                ('book_cost', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('room', models.CharField(blank=True, max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('term', models.CharField(blank=True, choices=[('None', None), ('Spring', 'Spring'), ('Fall', 'Fall'), ('Summer', 'Summer')], default='None', max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('note', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recorder', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=20)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6, null=True)),
                ('active', models.BooleanField(default=True)),
                ('mom_phone_num', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('dad_phone_num', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('transportation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=10)),
                ('freeBook', models.BooleanField(default=False)),
                ('freeClass', models.BooleanField(default=False)),
                ('cost', models.IntegerField(default=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='youthpalace.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='youthpalace.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6, null=True)),
                ('active', models.BooleanField(default=True)),
                ('phone_num', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='youthpalace.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='youthpalace.Teacher'),
        ),
    ]
