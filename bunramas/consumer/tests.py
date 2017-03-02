from django.test import TestCase
from provider.models import Offer
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

class OfferViewsTest(TestCase):

    def create_offer(self):
        tmp_starting_date = datetime.datetime(2016, 11, 6, hour=17, minute=0,
            second=0, microsecond=0, tzinfo=timezone.utc)#'2016-11-06 17:00:00'

        tmp_ending_date = datetime.datetime(2016, 11, 6, hour=18, minute=0,
            second=0, microsecond=0, tzinfo=timezone.utc)#'2016-11-06 18:00:00'

        offer = Offer(title = 'Title',
                      description = 'Description',
                      starting_date = tmp_starting_date,
                      expiration_date = tmp_ending_date,
                      location = 'Location',
                      provider = 'Provider')

        return offer


    def test_offer_list_view(self):
        offer = self.create_offer()
        url = reverse("offer-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(offer.title, resp.content)
