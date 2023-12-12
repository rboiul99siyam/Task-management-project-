from django.shortcuts import render , redirect

# Create your views here.
from . import forms
from . import models
def add_task(res):
    if res.method == 'POST':
        Model_form = forms.TaskModelForm(res.POST)
        if Model_form.is_valid():
            print(Model_form.cleaned_data)
            Model_form.save()
    else:
        Model_form = forms.TaskModelForm()
    return render(res,'add_task.html',{'form':Model_form})


