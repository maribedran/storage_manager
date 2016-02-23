# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase

from model_mommy import mommy

from src.storage.models import Purchase


class TestListPurchasesView(TestCase):

    def setUp(self):
        self.url = reverse('storage:list_purchases')

    def test_get_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_all_purchases_in_context(self):
        purchases = mommy.make(Purchase, _quantity=2)
        response = self.client.get(self.url)
        self.assertIn('object_list', response.context)
        for p in purchases:
            self.assertIn(p, response.context['object_list'])

    def test_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'list_purchases.html')
