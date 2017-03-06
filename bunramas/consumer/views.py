from django.views.generic.list import ListView
from django.utils import timezone

from provider.models import Offer

'''
Generic ListView of Offer.
'''
class OfferListView(ListView):
    '''
    template_name tells the ListView to use the consumer/offer_list.html template.
    '''
    template_name = "consumer/offer_list.html"
    model = Offer
    # This is used if we want to make change object_list to something more
    # readable.
    # context_object_name = 'offers'

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Offer.objects.filter(starting_date__lte=timezone.now(),
                                    expiration_date__gte=timezone.now())
