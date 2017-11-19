# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now


class Merchant(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=16)
  street_address = models.CharField(max_length=64)
  zip_code = models.CharField(max_length=5)
  joined = models.DateField(auto_now_add=True)
  verified = models.BooleanField(default=False)

  RESTO = 'RESTAURANT'
  OTHER = 'OTHER'
  CATEGORIES = (
    (RESTO, 'Restaurant'),
    (OTHER, 'Other'),
  )
  category = models.CharField(
    max_length=30,
    choices=CATEGORIES,
    default=RESTO,
  )



class Offer(models.Model):
  description = models.CharField(max_length=256)
  merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='offers')
  retail_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  contact_name = models.CharField(max_length=30)
  contact_phone = models.CharField(max_length=16)
  date_posted = models.DateTimeField()
  expiry = models.DateTimeField()
  # available is False when bid has been accepted for offer
  available = models.BooleanField(default=True)
  bid_accepted = models.BooleanField(default=False)

  def is_alive(self):
    time_now = now()
    return self.expiry > time_now and self.available



class Bid(models.Model):
  description = models.CharField(max_length=256)
  merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='bids')
  retail_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  contact_name = models.CharField(max_length=30)
  contact_phone = models.CharField(max_length=16)
  offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='bids')
  # accepted is True when bid is accepted for offer
  accepted = models.BooleanField(default=False)
  date_posted = models.DateTimeField()
  expiry = models.DateTimeField()

  def is_alive(self):
    time_now = now()
    return self.expiry > time_now and not self.accepted