from django.shortcuts import render , redirect

# Create your views here.
from . import forms
from . import models
from django.urls import reverse_lazy

from django.views.generic import CreateView

class Add_task(CreateView):
    model = models.TaskModels
    form_class = forms.TaskModelForm
    template_name = 'add_task.html'
    context_object_name = 'form'
    def get_success_url(self,*args, **kwargs):
        return reverse_lazy('add_task')
   
