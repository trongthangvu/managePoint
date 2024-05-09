from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to="users/%Y/%m/")




class Subject(models.Model):
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    midterm_grade = models.FloatField()
    final_grade = models.FloatField()
    is_locked = models.BooleanField(default=False)

class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
