from django.conf.urls import url

# from . import views
from consumer.views import OfferListView

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='offer-list'),
]
