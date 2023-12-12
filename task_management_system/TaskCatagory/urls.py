from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('taskCategory/',views.add_category,name='add_category'),
    path("edit_posts/<int:id>", views.edit_post, name="edit_post"),
    path('delete/<int:id>', views.delete, name='delete')
]
