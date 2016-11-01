from django.conf.urls import url

# from . import views
from home.views import OfferListView

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='offer-list'),
]
