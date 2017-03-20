from django.conf.urls import url
from provider.views import ProviderUserFormView, ProviderLoginFormView

urlpatterns = [
    url(r'^register/$', ProviderUserFormView.as_view(), name='register'),
    url(r'^login/$', ProviderLoginFormView.as_view(), name='login')
]
