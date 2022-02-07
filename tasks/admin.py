from django.contrib import admin

# Register your models here.

from tasks.models import Task
from tasks.models import TaskHistory

admin.sites.site.register(Task)
admin.sites.site.register(TaskHistory)
