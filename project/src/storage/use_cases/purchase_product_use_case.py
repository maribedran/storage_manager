# coding: utf-8
from decimal import  Decimal

from src.storage.models import Product, Purchase


class PurchaseProductUseCase(object):

    @classmethod
    def execute(cls, product_name, quantity, price):
        price = Decimal(price)
        purchase = Purchase.objects.create(
            product=product_name,
            quantity=quantity,
            price=price
        )
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'quantity': quantity,
                'average_price': price
            }
        )

        if not created:
            original_price = product.average_price
            original_qtt = product.quantity
            new_qtt = original_qtt + purchase.quantity
            new_price = (original_price * original_qtt + purchase.price * purchase.quantity) / new_qtt

            product.average_price = new_price
            product.quantity = new_qtt
            product.save()
