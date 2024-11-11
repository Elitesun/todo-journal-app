from django.contrib import admin  # Importing admin module from django.contrib
from .models import Task , Journal  # Importing Task model from the current app's models

# Registering the Task model with the admin site
admin.site.register(Task)
admin.site.register(Journal)
