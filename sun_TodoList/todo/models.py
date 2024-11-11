from django.db import models
from django.contrib.auth.models import User

# Task model to store todo list items
class Task(models.Model):
    # ForeignKey relationship with User model, allows null/blank for flexibility
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Title field for the task, required, max 200 chars
    title = models.CharField(max_length=200, null=True)
    
    # Optional description field for additional task details
    description = models.TextField(null=True, blank=True)
    
    # Boolean field to mark task completion status
    complete = models.BooleanField(default=False)
    
    # Automatically set timestamp when task is created
    created = models.DateTimeField(auto_now_add=True)
    
    # String representation of Task object
    def __str__(self):
        return self.title
    
    # Meta class to specify model options
    class Meta:
        # Order tasks by completion status (incomplete first)
        ordering = ['complete']

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
