from django.shortcuts import render, redirect

#django already has user forms and we can directly import them(not using here)
#from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
# available options:
# messages.debug
# messages.info
# messages.error
# messages.success
# messages.warning

from django.contrib.auth.decorators import login_required

#the new created form with inheritance from UserCreationForm 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()#to save to db(it automatically hashes password and stuff)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)