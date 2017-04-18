from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import Provider
from .forms import ProviderUserForm, ProviderLoginForm

'''
View for creating a provider user
Creates an user and adds it to provider group
'''
class ProviderUserFormView(FormView):
    form_class = ProviderUserForm
    template_name = "provider/registration_form.html"

    '''
    Display a blank form
    '''
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    '''
    Process form data
    '''
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            #create a new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            new_user = User.objects.create_user(username=username, password=password, email=email)
            group = Group.objects.get(name='provider')
            new_user.groups.add(group)
            new_user.save()

            #create a new profile
            company_name = form.cleaned_data['company_name']
            Provider.objects.create(user = new_user, company_name=company_name)
            new_user.provider.save()

            #redirect to login
            return redirect('provider:login')
        #if form is invalid
        return render(request, self.template_name, {'form':form})

'''
View for logging in as a provider
'''
class ProviderLoginFormView(FormView):
    form_class = ProviderLoginForm
    template_name = "provider/login_form.html"

    '''
    Display a blank form
    '''
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    '''
    Process form data
    '''
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)

            #return redirect('provider:register') # just for testing
            #redirect to profile - to do
        #if form is invalid
        return render(request, self.template_name, {'form':form})
