from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

#inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()#required=False can also be put inside, default is true

    #class Meta gives us nested namespace for configurations, keeps the configurations in one place
    class Meta:
        #model affected is User
        model = User
        #and fields of form are fields here 
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']