from django.db import models
from django.contrib.auth.models import User


class Producer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='kakala')

    def __str__(self) -> str:
        return self.name


class Products(models.Model):

    product_categories = [
        ('DI', 'digitals'),
        ('HO', 'house'),
        ('PL', 'plants'),
        ('CL', 'clothing'),
        ('SP', 'sport'),
        ('MA', 'makeup'),
        ('UN', 'uncategorized'),
        ('BK', 'books'),
    ]

    name = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    producer = models.ManyToManyField(Producer)
    entity = models.PositiveBigIntegerField(default=0)
    categorie = models.CharField(choices=product_categories, max_length=30, default='UN')

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_amount = models.PositiveIntegerField(default=10000)

    def __str__(self) -> str:
        return str(self.user)


class OnDemand(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    replica = models.PositiveIntegerField(default=1)
