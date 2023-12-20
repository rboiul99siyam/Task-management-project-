from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('taskCategory/',views.Add.as_view(),name='add_category'),
    path("edit_posts/<int:id>", views.Update.as_view(), name="edit_post"),
    path('delete/<int:id>', views.deteleNow.as_view(), name='delete')
]
