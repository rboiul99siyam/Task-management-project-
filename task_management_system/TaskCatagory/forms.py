from django import forms

from TaskCatagory.models import TaskCategory

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'