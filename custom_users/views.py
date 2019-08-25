from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .forms import SignUpForm


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration Successful!')
            return redirect('login')

    else:
        form = SignUpForm()

    template = 'custom_users/registration.html'
    context = {'form': form}

    return render(request, template, context)

