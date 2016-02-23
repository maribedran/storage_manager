# coding: utf-8
from django.views.generic import ListView

from src.storage.models import Purchase


class ListPurchasesView(ListView):
    queryset = Purchase.objects.all()
    template_name = 'list_purchases.html'
