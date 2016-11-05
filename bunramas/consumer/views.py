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

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
