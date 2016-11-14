from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_offer/$', views.add_offer, name = 'add_offer')
]
