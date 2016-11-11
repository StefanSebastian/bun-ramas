from django.test import TestCase
from provider.models import Offer
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

class OfferTest(TestCase):
    '''
    Creates an instance of Offer
    '''
    def create_offer(self,
                     title = 'Title',
                     description = 'Description',
                     starting_date = datetime(2016,11,6,17,0,0, tzinfo=timezone.utc),
                     expiration_date = datetime(2016,11,6,18,0,0, tzinfo=timezone.utc),
                     location = 'Location',
                     provider = 'Provider'):
        return Offer.objects.create(title = title, description = description, starting_date = starting_date,
                     expiration_date = expiration_date, location = location, provider = provider)

    '''
    Tests the creation of an Offer
    '''
    def test_create(self):
        offer = self.create_offer()
        self.assertTrue(isinstance(offer, Offer))
        self.assertEqual('Title', offer.title)
        self.assertEqual('Description', offer.description)
        self.assertEqual(datetime(2016,11,6,17,0,0, tzinfo=timezone.utc), offer.starting_date)
        self.assertEqual(datetime(2016,11,6,18,0,0, tzinfo=timezone.utc), offer.expiration_date)
        self.assertEqual('Location', offer.location)
        self.assertEqual('Provider', offer.provider)

    '''
    Tests the offer's to string method
    '''
    def test_string(self):
        offer = self.create_offer(title = 'Title')
        self.assertEqual('Title', offer.__str__())

    '''
    Tests the date validation
    '''
    def test_valid_dates(self):
        offer1 = self.create_offer(starting_date = datetime(2016,12,4,16,0,0, tzinfo=timezone.utc),
                                   expiration_date = datetime(2016, 12, 4, 17, 0, 0, tzinfo=timezone.utc))

        try:
            offer1.clean()
            self.assertTrue(True)
        except ValidationError as e:
            self.assertTrue(False)

        offer2 = self.create_offer(starting_date = datetime(2016,12,4,16,20,10, tzinfo=timezone.utc),
                                   expiration_date = datetime(2016, 12, 4, 13, 0, 0, tzinfo=timezone.utc))
        try:
            offer2.clean()
            self.assertTrue(False)
        except ValidationError as e:
            self.assertTrue(True)
