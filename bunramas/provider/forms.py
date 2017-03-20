from django.contrib.auth.models import User
from django import forms
from provider.models import Provider
from django.contrib.auth import authenticate

'''
Form for creating a user
'''
class ProviderUserForm(forms.ModelForm):
    '''
    Password field
    '''
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

'''
Form for logging in a provider user
'''
class ProviderLoginForm(forms.Form):
    '''
    Username field
    '''
    username = forms.CharField(widget=forms.TextInput())

    '''
    Password field
    '''
    password = forms.CharField(widget=forms.PasswordInput)

    '''
    Validates credentials - overrides the forms.Form clean method 
    throws ValidationError
    '''
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        '''
        Checks if valid user
        '''
        if not user:
            raise forms.ValidationError("Invalid username or password. Please try again.")

        '''
        Checks if active user (not banned)
        '''
        if not user.is_active:
            raise forms.ValidationError("Your username is not active.")

        '''
        Checks if user is part of provider group
        '''
        if not user.groups.filter(name='provider').exists():
            raise forms.ValidationError("You must have a provider account")

        return self.cleaned_data
