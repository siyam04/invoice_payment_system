from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        """Metadata Class"""
        ordering = ['-id']

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name


class Invoice(models.Model):

    CURRENCIES = (
        ('Euros', 'Euros'),
        ('USD', 'USD'),
        ('Pounds', 'Pounds'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=20, choices=CURRENCIES, default='Euros')
    date = models.DateField(null=True, blank=True)
    item_code = models.CharField(max_length=10)
    item_description = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit_price = models.FloatField(default=0.00)
    discount = models.FloatField()
    # discount = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.item_code

    @property
    def total(self):
        total_price = self.quantity * self.unit_price - (self.discount / 100)
        # modification = '{:.2f}'.format(total_price)
        # modification = round(total_price, 2)
        return total_price


# class Order(models.Model):
#     product_name = models.CharField(max_length=150)
#     category = models.CharField(max_length=150)
#     description = models.TextField(max_length=500)
#
#     class Meta:
#         ordering = ['-id']
#
#     def __str__(self):
#         return self.product_name

