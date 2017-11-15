# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils.timezone import timedelta

from tradefood.utilities import is_alive
from tradefood.forms import *

# Create your views here.

def see_all_offers(request):
  offers = Offer.objects.filter(date_posted)

def submit_offer(request):
  if request.method == 'POST':
    form = OfferForm(request.POST)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      merch = Merchant.objects.get(user=u)

      form_data = form.cleaned_data
      offer_expiry = form_data['date_posted'] + timedelta(form_data['duration'])

      offer = Offer.objects.create(
        description=form_data['description'],
        merchant=merch,
        retail_value=form_data['retail_value'],
        contact_name=form_data['contact_name'],
        contact_phone=form_data['contact_phone'],
        expiry=offer_expiry,
      )
  else:
    form = OfferForm()
  return render(request, 'tradefood/all_offers.html', {'form': form})

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      