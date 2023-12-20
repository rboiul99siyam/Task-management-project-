from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from . import forms
from . import models

from django.views.generic import CreateView ,UpdateView ,DeleteView

class Add(CreateView):
    model = models.TaskCategory
    form_class =  forms.TaskCategoryForm
    template_name = 'add_category.html'
    context_object_name = 'form'
    def get_success_url(self , *args, **kwargs):
        return reverse_lazy('add_category')




class Update (UpdateView):
    model = models.TaskCategory
    form = forms.TaskCategoryForm
    template_name = 'add_task.html'
    context_object_name = 'form'
    pk_url_kwarg = 'id'
    fields = '__all__'
    def get_success_url(self,*args, **kwargs):
        return reverse_lazy('showtask')




class deteleNow(DeleteView):
    model = models.TaskCategory
    template_name = 'add_category.html'
    pk_url_kwarg = 'id'
    def get_success_url(self,*args,**Kwargs):
        return reverse_lazy('showtask')

