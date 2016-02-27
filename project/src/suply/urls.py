from django.conf.urls import url

from .views import CheckInProductView


urlpatterns = [
    url(r'^check_in', CheckInProductView.as_view(), name='check_in_product'),
]
