# coding: utf-8
from django.test import TestCase

from src.storage.use_cases import PurchaseProductUseCase
from src.storage.models import Product, Purchase


class PurchaseProductUseCaseTest(TestCase):

    def test_purchase_new_product(self):
        PurchaseProductUseCase.execute('Product', 1, 10.00)

        self.assertEqual(1, Purchase.objects.count())
        self.assertEqual(1, Product.objects.count())
        self.assertEqual(10.00, Product.objects.get().average_price)
        self.assertEqual(1, Product.objects.get().quantity)

    def test_purchase_existing_product(self):
        product = Product.objects.create(name='Product', quantity=10, average_price=10.00)
        PurchaseProductUseCase.execute('Product', 5, 15.00)

        self.assertEqual(1, Purchase.objects.count())
        self.assertEqual(1, Product.objects.count())
        self.assertEqual(11.67, float(Product.objects.get().average_price))
        self.assertEqual(15, Product.objects.get().quantity)
