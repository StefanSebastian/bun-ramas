from django.test import TestCase
from provider.models import Offer
from django.utils import timezone
import datetime

class OfferTest(TestCase):

    def test_create(self):
        # pass
        tmp_starting_date = datetime.datetime(2016, 11, 6, hour=17, minute=0,
            second=0, microsecond=0)#'2016-11-06 17:00:00',
        print(timezone.is_aware(tmp_starting_date))
        tmp_starting_date = timezone.make_aware(tmp_starting_date)
        print(timezone.is_aware(tmp_starting_date))

        tmp_ending_date = datetime.datetime(2016, 11, 6, hour=18, minute=0,
            second=0, microsecond=0)#'2016-11-06 18:00:00',
        tmp_ending_date = timezone.make_aware(tmp_ending_date)

        offer = Offer(title = 'Title',
                      description = 'Description',
                      starting_date = tmp_starting_date,
                      expiration_date = tmp_ending_date,
                      location = 'Location',
                      provider = 'Provider')

        # print(timezone.is_aware(offer.starting_date))
        self.assertEqual('Title', offer.title)
        self.assertEqual('Description', offer.description)
        self.assertEqual(tmp_starting_date, offer.starting_date)
        self.assertEqual(tmp_ending_date, offer.expiration_date)
        self.assertEqual('Location', offer.location)
        self.assertEqual('Provider', offer.provider)
