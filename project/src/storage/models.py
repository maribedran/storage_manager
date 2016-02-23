from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200, unique=True)
    quantity = models.PositiveIntegerField()
    average_price = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):

    product = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(db_index=True, auto_now_add=True)
