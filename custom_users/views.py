from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Profile
from .forms import SignUpForm, ProfileForm


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    template = 'custom_users/registration.html'
    context = {'form': form}

    return render(request, template, context)


@login_required(login_url='login')
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('custom_users:profile_details', id=profile.id)

    template = 'custom_users/profile_create.html'
    context = {'form': ProfileForm()}

    return render(request, template, context)


@login_required(login_url='login')
def profile_details(request, id=None):
    profile = get_object_or_404(Profile, id=id)

    context = {'profile': profile}
    template = 'custom_users/profile_details.html'

    return render(request, template, context)


@login_required(login_url='login')
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # messages.success(request, 'Profile Updated for {}'.format(request.user.username), extra_tags='html_safe')

            # return redirect('user/profile-detail/')
            return redirect('custom_users:profile_details', id=profile.id)

    context = {'form':form}
    template = 'custom_users/profile_edit.html'

    return render(request, template, context)

