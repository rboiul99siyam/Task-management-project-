from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from . import models


def add_category(res):
    if res.method == "POST":
        Model_cata = forms.TaskCategoryForm(res.POST)
        if Model_cata.is_valid():
            print(Model_cata.cleaned_data)
            Model_cata.save()
            return redirect("add_category")
    else:
        Model_cata = forms.TaskCategoryForm()
    return render(res, "add_category.html", {"form": Model_cata})


def edit_post(res, id):
    post = models.TaskCategory.objects.get(pk=id)
    model_cata = forms.TaskCategoryForm(instance=post)
    if res.method == "POST":
        model_cata = forms.TaskCategoryForm(res.POST, instance=post)
        if model_cata.is_valid():
            model_cata.save()
            return redirect('showtask')
    else:
        model_cata = forms.TaskCategoryForm()
    return render(res,'add_task.html',{'form':model_cata})


def delete(res, id):
    post = models.TaskCategory.objects.get(pk=id)
    post.delete()
    return redirect('showtask')