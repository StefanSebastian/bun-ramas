from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from provider.models import Offer
from consumer.models import Consumer
from consumer.forms import ConsumerUserForm, ConsumerLoginForm

'''
Generic ListView of Offer.
'''
class OfferListView(ListView):
    '''
    template_name tells the ListView to use the consumer/offer_list.html template.
    '''
    template_name = "consumer/offer_list.html"
    model = Offer

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

'''
View for creating a consumer user
Creates an user and adds it to consumer group
'''
class ConsumerUserFormView(FormView):
    form_class = ConsumerUserForm
    template_name = "consumer/registration_form.html"

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
            group = Group.objects.get(name='consumer')
            new_user.groups.add(group)
            new_user.save()

            #create a new profile
            Consumer.objects.create(user = new_user)
            new_user.consumer.save()

            #redirect to login
            return redirect('consumer:login')
        #if form is invalid
        return render(request, self.template_name, {'form':form})

'''
View for logging in as a consumer
'''
class ConsumerLoginFormView(FormView):
    form_class = ConsumerLoginForm
    template_name = "consumer/login_form.html"

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

            #redirect to profile - to do
        #if form is invalid
        return render(request, self.template_name, {'form':form})
