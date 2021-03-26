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
from .forms import UserRegisterForm


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
    return render(request, 'users/profile.html')