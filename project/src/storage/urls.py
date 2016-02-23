from django.conf.urls import include, url

from .views import ListProductsView, ListPurchasesView


urlpatterns = [
    url(r'^$', ListProductsView.as_view(), name='list_products'),
    url(r'^purchases/$', ListPurchasesView.as_view(), name='list_purchases'),
]
