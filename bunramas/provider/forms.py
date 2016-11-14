from django import forms
from provider.models import Offer

class OfferInsertForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'description', 'starting_date', 'expiration_date', 'location']
        help_texts = {
            'title' : 'First thing the clients will see.',
            'description' : 'Describe your offer.',
            'starting_date' : 'When does the offer become valid? Insert a date with the following format: YYYY-MM-DD HH:MM:SS',
            'expiration_date' : 'When does the offer expire? Insert a date with the following format: YYYY-MM-DD HH:MM:SS',
            'location' : 'Where can the clients find you?'
        }
