from django import forms
from TaskModel.models import TaskModels

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModels
        fields = '__all__'
        widgets = {
            'task_title': forms.TextInput(attrs={'placeholder':'Enter Your Title Name !'}),
            'Task_Assign_Date': forms.TimeInput(attrs={'type':'date'})
        }
