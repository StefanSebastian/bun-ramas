from django.test import TestCase
from provider.models import Offer
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

class OfferViewsTest(TestCase):
    '''
    Creates an offer.

    Parameters
    ----------
    starting_date : datetime.datetime
        An object containing information about the start time and date of an
        offer.
    ending_date : datetime.datetime
        An object containing information about the end time and date of an
        offer.
    '''
    def create_offer(self, starting_date, ending_date):

        offer = Offer(title = 'Title',
                      description = 'Description',
                      starting_date = starting_date,
                      expiration_date = ending_date,
                      location = 'Location',
                      provider = 'Provider')

        return offer

    def setUp(self):
        starting_date = datetime.datetime(2016, 11, 6, hour=17, minute=0,
            second=0, microsecond=0, tzinfo=timezone.utc)#'2016-11-06 17:00:00'

        ending_date = datetime.datetime(2016, 11, 6, hour=18, minute=0,
            second=0, microsecond=0, tzinfo=timezone.utc)#'2016-11-06 18:00:00'

        Offer.objects.create(title = 'Past offer',
                             description = 'Description',
                             starting_date = starting_date,
                             expiration_date = ending_date,
                             location = 'Location',
                             provider = 'Provider')

        starting_date = timezone.now()
        ending_date = timezone.now()

        # Make sure the current offer has still not expired.
        ending_date = ending_date.replace(year = ending_date.year + 1)

        Offer.objects.create(title = 'Current offer 1',
                             description = 'Description curr 1',
                             starting_date = starting_date,
                             expiration_date = ending_date,
                             location = 'Location curr 1',
                             provider = 'Provider curr 1')

        starting_date = timezone.now()
        ending_date = timezone.now()

        # Make sure the current offer has still not expired.
        starting_date = starting_date.replace(year = starting_date.year - 1)
        ending_date = ending_date.replace(year = ending_date.year + 2)

        Offer.objects.create(title = 'Current offer 2',
                             description = 'Description curr 2',
                             starting_date = starting_date,
                             expiration_date = ending_date,
                             location = 'Location curr 2',
                             provider = 'Provider curr 2')


        starting_date = timezone.now()
        ending_date = timezone.now()

        # Make sure the current offer has still not expired.
        starting_date = starting_date.replace(year = starting_date.year + 1)
        ending_date = ending_date.replace(year = ending_date.year + 2)

        Offer.objects.create(title = 'Future offer',
                             description = 'Description future',
                             starting_date = starting_date,
                             expiration_date = ending_date,
                             location = 'Location future',
                             provider = 'Provider future')

    def test_offer_list_view(self):
        url = reverse("offer-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # Encoding the strings is necessary because the test function requires
        # a byte-array like object.
        self.assertIn('Current offer 1'.encode('utf-8'), resp.content)
        self.assertIn('Current offer 2'.encode('utf-8'), resp.content)
        self.assertNotIn('Past offer'.encode('utf-8'), resp.content)
        self.assertNotIn('Future offer'.encode('utf-8'), resp.content)

    def test_offer_detail_view(self):
        curr_object_1 = Offer.objects.get(title='Current offer 1')
        url = reverse('offer-detail', args=(curr_object_1.pk,
                                            curr_object_1.slug,)
                    )
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        
        self.assertIn('Current offer 1'.encode('utf-8'), resp.content)
        self.assertNotIn('Current offer 2'.encode('utf-8'), resp.content)
        self.assertNotIn('Past offer'.encode('utf-8'), resp.content)
        self.assertNotIn('Future offer'.encode('utf-8'), resp.content)
