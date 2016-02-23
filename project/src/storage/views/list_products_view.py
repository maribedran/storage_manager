# coding: utf-8
from django.views.generic import ListView

from src.storage.models import Product


class ListProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'list_products.html'
