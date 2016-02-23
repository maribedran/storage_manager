from django.conf.urls import include, url

from .views import ListProductsView

urlpatterns = [
    url(r'^$', ListProductsView.as_view(), name='list_products'),
]


