# coding: utf-8
from django.test import TestCase

from src.suply.forms import CheckInProductForm


class TestCheckInProductForm(TestCase):

    def setUp(self):
        self.form_class = CheckInProductForm
        self.data = {
            'product_name': 'Product',
            'quantity': 100,
            'price': 1.99
        }

    def test_required_fields(self):
        required_fields = [
            'product_name',
            'quantity',
            'price',
        ]
        form = self.form_class({})
        self.assertFalse(form.is_valid())
        for field in required_fields:
            self.assertIn(field, form.errors.keys())

    def test_forn_valid(self):
        form = self.form_class(self.data)
        self.assertTrue(form.is_valid())
