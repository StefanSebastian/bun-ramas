from django.conf.urls import url

from provider.views import AddOfferView
from provider.views import SuccessOfferAdditionView

urlpatterns = [
    url(r'^add_offer/$', AddOfferView.as_view(), name='add_offer'),
    url(r'^add_offer/success_add/$', SuccessOfferAdditionView.as_view())
]
