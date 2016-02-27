# coding: utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import FormView

from src.suply.forms import CheckInProductForm


class CheckInProductView(FormView):
    template_name = 'check_in_product.html'
    form_class = CheckInProductForm

    def form_valid(self, form):
        message = '%d units of %s checked in in storage.' \
                   % (form.cleaned_data['quantity'], form.cleaned_data['product_name'])
        messages.success(self.request, messages)
        return self.get(self.request)
