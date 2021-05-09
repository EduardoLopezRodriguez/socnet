from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}, ahora puedes iniciar sesión.')

            return redirect('login')

    else:

        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
            
        user_form    = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Cuenta actualizada')
            return redirect('profile')

    else:
        user_form    = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def delete_user(request):

    if request.method == 'POST':

        form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('home')
    else:
        form = UserDeleteForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'users/delete_user.html', context)