from django import forms
from .models import UserTweets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetsForm(forms.ModelForm):
    class Meta:
        model = UserTweets
        fields = ['text', 'photo']  

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
