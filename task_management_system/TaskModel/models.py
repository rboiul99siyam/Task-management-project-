from django.db import models

# Create your models here.
class TaskModels(models.Model):
    task_title = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField()

    def __str__(self) -> str:
        return self.task_title