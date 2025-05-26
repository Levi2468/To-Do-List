from django.db import models


class LoginMatch(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


class Tasktodo(models.Model):
    Title = models.CharField(max_length=20)
    Task = models.TextField()
