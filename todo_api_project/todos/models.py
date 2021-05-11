from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return '@'+self.username

class Todo(models.Model):
    """Model to store Todos"""

    task = models.CharField(max_length=500)
    created_by = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.task
