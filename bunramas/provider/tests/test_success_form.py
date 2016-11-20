from django.test import TestCase

class SuccessFormTest(TestCase):
    def test_call_view_loads(self):
        response = self.client.get('/provider/add_offer/success_add/')

        '''
        HTTP_200_OK status code, the request has succeeded
        '''
        self.assertEqual(response.status_code, 200)

        '''
        Used the corect template
        '''
        self.assertTemplateUsed(response, 'provider/success_add.html')
