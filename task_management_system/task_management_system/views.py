from django.shortcuts import render

from TaskCatagory.models import TaskCategory
from django.views.generic import TemplateView
def home(res):
    data = TaskCategory.objects.all()
    return render(res,'home.html' , {'data':data})

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TaskCategory.objects.all()
        return context