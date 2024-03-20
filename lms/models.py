from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    created_at = models.DateTimeField(auto_now_add=True)

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()
    duration = models.DurationField()
    max_score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Grade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Communication(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)