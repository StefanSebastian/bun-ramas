from django.conf.urls import url
from consumer.views import ConsumerUserFormView, ConsumerLoginFormView

urlpatterns = [
    url(r'^register/$', ConsumerUserFormView.as_view(), name='register'),
    url(r'^login/$', ConsumerLoginFormView.as_view(), name='login')
]
