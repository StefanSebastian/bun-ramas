from django import forms
from provider.models import Offer

'''
Form used to insert an Offer
'''
class OfferInsertForm(forms.ModelForm):
    class Meta:
        '''
        Model from which the form is created
        '''
        model = Offer

        '''
        Fields from the model inserted in the form
        '''
        fields = ['title', 'description', 'starting_date', 'expiration_date', 'location']

        '''
        Helping text for completing the form
        '''
        help_texts = {
            'title' : 'First thing the clients will see.',
            'description' : 'Describe your offer.',
            'starting_date' : 'When does the offer become valid? Insert a date with the following format: YYYY-MM-DD HH:MM:SS',
            'expiration_date' : 'When does the offer expire? Insert a date with the following format: YYYY-MM-DD HH:MM:SS',
            'location' : 'Where can the clients find you?'
        }
