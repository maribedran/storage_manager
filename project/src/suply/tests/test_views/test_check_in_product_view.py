# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from src.suply.views import CheckInProductView


class TestCheckInProductView(TestCase):

    def setUp(self):
        self.url = reverse('suply:check_in_product')
        self.data = {
            'product_name': 'Product',
            'quantity': 100,
            'price': 1.99
        }

    def test_get_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'check_in_product.html')

    def test_post_correct_data(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(200, response.status_code)
        self.assertIn('messages', response.context)

    def test_post_false_data(self):
        fields = [
            'product_name',
            'quantity',
            'price'
        ]
        response = self.client.post(self.url, {})
        self.assertEqual(200, response.status_code)
        for field in fields:
            self.assertIn(field, response.context['form'].errors)
