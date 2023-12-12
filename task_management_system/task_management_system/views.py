from django.shortcuts import render

from TaskCatagory.models import TaskCategory
def home(res):
    data = TaskCategory.objects.all()
    return render(res,'home.html' , {'data':data})