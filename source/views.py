from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


# def home(request):
#     template = 'home.html'
#     return render(request, template)


