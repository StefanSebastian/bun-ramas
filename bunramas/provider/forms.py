from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from provider.models import Provider

'''
Form for creating a user
'''
class ProviderUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
