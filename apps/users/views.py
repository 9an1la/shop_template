from io import BytesIO

import requests
from allauth.socialaccount.models import SocialAccount
from django.core import files
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from apps.users.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'users/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно изменён')
        else:
            messages.error(request, 'Ошибка изменения профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@receiver(user_signed_up)
def user_signed_up(request, user, **kwargs):
    social_account = SocialAccount.objects.get(user=user)
    if social_account.provider == 'github':
        data = social_account.extra_data
        avatar_url = data['avatar_url']
        response = requests.get(avatar_url)
        if response.status_code == 200:
            avatar_data = BytesIO()
            avatar_data.write(response.content)
            avatar_name = avatar_url.split('/')[-1]
            Profile.objects.create(user=user, photo=files.File(file=avatar_data, name=avatar_name))
        else:
            Profile.objects.create(user=user)
    else:
        Profile.objects.create(user=user)
