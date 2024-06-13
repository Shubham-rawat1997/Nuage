from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_class = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    course_class = models.CharField(max_length=50)
    lecture_hours = models.IntegerField()
    submitted_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

class AttendanceLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)    


