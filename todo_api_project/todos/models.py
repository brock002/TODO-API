from django.db import models

# Create your models here.

class Todo(models.Model):
    """Model to store Todos"""

    task = models.CharField(max_length=500)
    is_finished = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.task
