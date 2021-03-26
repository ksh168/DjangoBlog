from django.shortcuts import render, redirect

#django already has user forms and we can directly import them
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
# available options:
# messages.debug
# messages.info
# messages.error
# messages.success
# messages.warning

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()#to save to db(it automatically hashes password and stuff)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})