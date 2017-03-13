from django.conf.urls import url
from provider.views import ProviderUserFormView

urlpatterns = [
    url(r'^register/$', ProviderUserFormView.as_view(), name='register')
]
