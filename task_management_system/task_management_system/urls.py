from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('taskModel/', include('TaskModel.urls')),
    path('taskCategory/', include('TaskCatagory.urls')),
    path('', views.home, name='showtask' )
]
