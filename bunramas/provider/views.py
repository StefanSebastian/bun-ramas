from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import Group, User

from .models import Provider
from .forms import ProviderUserForm

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
            new_user = User.objects.create_user(**form.cleaned_data)
            group = Group.objects.get(name='provider')
            new_user.groups.add(group)
            new_user.save()

            #create a new profile
            Provider.objects.create(user = new_user)
            new_user.provider.save()
            #will redirect to profile update page - so company name is not left blank 
        #if form is invalid
        return render(request, self.template_name, {'form':form})
