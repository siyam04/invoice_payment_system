from django.shortcuts import render
from django.views.generic.base import TemplateView

from custom_users.models import Profile


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = ''

    template = 'home.html'
    context = {'profile': profile}

    return render(request, template, context)


# class HomeView(TemplateView):
#     template_name = 'home.html'
