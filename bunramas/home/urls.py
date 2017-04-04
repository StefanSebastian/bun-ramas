from django.conf.urls import url

# from . import views
from consumer.views import OfferListView
from consumer.views import OfferDetailView

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='offer-list'),
    url(r'^offers/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', OfferDetailView.as_view(), name='offer-detail'),
    # url(r'^offers/(?P<pk>[0-9]+)/$', OfferDetailView.as_view(), name='offer-detail'),
]
