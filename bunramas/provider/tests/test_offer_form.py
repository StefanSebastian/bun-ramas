from django.test import TestCase
from provider.forms import OfferInsertForm

class OfferFormTest(TestCase):
    '''
    Tests the valid form function
    '''
    def test_valid_form(self):
        form_data = {'title':'title', 'description':'description', 'location':'location',
        'starting_date':'2016-11-11 17:00:00', 'expiration_date':'2016-11-11 19:22:22'}
        form = OfferInsertForm(data=form_data)
        self.assertTrue(form.is_valid())

    '''
    Tests the offer form view
    '''
    def test_call_view_loads(self):
        response = self.client.get('/provider/add_offer/')

        '''
        HTTP_200_OK status code, the request has succeeded
        '''
        self.assertEqual(response.status_code, 200)

        '''
        Used the corect template
        '''
        self.assertTemplateUsed(response, 'provider/add_offer.html')

    '''
    Tests whether the post method fails on empty forms
    '''
    def test_call_view_fails_blank(self):
        response = self.client.post('/provider/add_offer/', {})
        self.assertFormError(response, 'form', 'expiration_date', 'This field is required.')
        self.assertFormError(response, 'form', 'starting_date', 'This field is required.')
        self.assertFormError(response, 'form', 'title', 'This field is required.')
        self.assertFormError(response, 'form', 'description', 'This field is required.')
        self.assertFormError(response, 'form', 'location', 'This field is required.')

    '''
    Tests whether the post methos validates datetime fields
    '''
    def test_call_view_fails_invalid_date(self):
        form_data = {'title':'title', 'description':'description', 'location':'location',
        'starting_date':'a', 'expiration_date':'223'}
        response = self.client.post('/provider/add_offer/', form_data)
        self.assertFormError(response, 'form', 'expiration_date', 'Enter a valid date/time.')
        self.assertFormError(response, 'form', 'starting_date', 'Enter a valid date/time.')

    '''
    Tests the validity of dates inserted
    '''
    #def test_call_view_fails_wrong_dates(self):
        #to implement when I get date validation from story-offer
