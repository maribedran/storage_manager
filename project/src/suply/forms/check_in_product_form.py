# coding: utf-8
from django import forms


class CheckInProductForm(forms.Form):

    product_name = forms.CharField(max_length=200)
    quantity = forms.IntegerField()
    price = forms.FloatField()
