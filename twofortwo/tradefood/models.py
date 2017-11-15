# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now, timedelta


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
  GEN_FOOD = 'GEN FOOD'
  CATEGORIES = (
    (RESTO, 'Restaurant'),
    (GEN_FOOD, 'Food'),
  )
  category = models.CharField(
    max_length=30,
    choices=CATEGORIES,
    default=RESTO,
  )



class Offer(models.Model):
  description = models.CharField(max_length=256)
  merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
  retail_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  contact_name = models.CharField(max_length=30)
  contact_phone = models.CharField(max_length=16)
  date_posted = models.DateTimeField(auto_now_add=True)
  expiry = models.DateTimeField()

  THIRTY_MIN = 0.5/24.0
  ONE_HR = 1.0/24.0
  TWO_HRS = 2.0/24.0
  THREE_HRS = 3.0/24.0
  DURATION_CHOICES = (
    (THIRTY_MIN, '30 minutes'),
    (ONE_HR, '1 hour'),
    (TWO_HRS, '2 hours'),
    (THREE_HRS, '3 hours'),
  )
  duration = models.FloatField(
    choices=DURATION_CHOICES,
    default=ONE_HR,
  )

  # expiry = date_posted + timedelta(duration)

  # def is_alive(self):
  #   time_now = now()
  #   expiry = self.date_posted + timedelta(self.duration)
  #   return expiry > time_now



class Bid(models.Model):
  description = models.CharField(max_length=256)
  merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
  retail_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
  contact_name = models.CharField(max_length=30)
  contact_phone = models.CharField(max_length=16)
  offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
  accepted = models.BooleanField(default=False)
  date_posted = models.DateTimeField(auto_now_add=True)
  expiry = models.DateTimeField()

  THIRTY_MIN = 0.5/24.0
  ONE_HR = 1.0/24.0
  TWO_HRS = 2.0/24.0
  THREE_HRS = 3.0/24.0
  DURATION_CHOICES = (
    (THIRTY_MIN, '30 minutes'),
    (ONE_HR, '1 hour'),
    (TWO_HRS, '2 hours'),
    (THREE_HRS, '3 hours'),
  )
  duration = models.FloatField(
    choices=DURATION_CHOICES,
    default=ONE_HR,
  )

  # expiry = date_posted + timedelta(duration)

  # def is_alive(self):
  #   time_now = now()
  #   return self.expiry > time_now

  # def is_alive(self):
  #   time_now = now()
  #   expiry = self.date_posted + timedelta(self.duration)
  #   return expiry > time_now
