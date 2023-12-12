from django.contrib import admin

# Register your models here.
from TaskModel.models import TaskModels
admin.site.register(TaskModels)