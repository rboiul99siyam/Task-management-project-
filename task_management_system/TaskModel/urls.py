from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("Add_task/", views.add_task, name="add_task"),
   
]
