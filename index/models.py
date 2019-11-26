from django.db import models
import uuid

# Create your models here.
class Account(models.Model):

    servers = (
        ('EUW', 'EUW'),
        ('EUNE', 'EUNE'),
        ('NA', 'NA'),
    )

    Username = models.CharField(unique=True, max_length=100)
    Password = models.CharField(max_length=100)
    Server = models.CharField(
        max_length=6, choices=servers, )
    Buyer_Email = models.EmailField(null=True)
    UUID = models.CharField(max_length=36)
    bought = models.BooleanField(default=False)
    StripePaymentID = models.CharField(max_length=500)

class Cart(models.Model):
    quantity = models.IntegerField()
    UUID = models.CharField(max_length=36)
    server = models.CharField(max_length=10)
    Buyer_Email = models.EmailField(null=True)
    StripePaymentID = models.CharField(max_length=500)
    PaymentConfirmed = models.BooleanField(default=False)