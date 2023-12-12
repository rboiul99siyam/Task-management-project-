from django.db import models

# Create your models here.

from TaskModel.models import TaskModels
class TaskCategory(models.Model):
    Category_Name = models.CharField(max_length=50)
    TaskModel = models.ManyToManyField(TaskModels)
    

    def __str__(self) -> str:
        return self.Category_Name