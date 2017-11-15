# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.utils.timezone import timedelta, now

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from tradefood.forms import *
from tradefood.models import Merchant, Offer, Bid

# Create your views here.

def all_offers(request):
  offers = Offer.objects.filter(expiry__gt=now().date())
  return render(request, 'tradefood/offers.html', {'offers': offers})

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
  return render(request, 'tradefood/trade.html', {'form': form})

def register(request):
  if request.method == 'POST':
    form_data = request.POST

    # need to validate data before creating
    new_user = User.objects.create_user(
      form_data['username'],
      password=form_data['password'],
    )

    new_merchant = Merchant.objects.create(
      user=new_user,
      email=form_data['email'],
      phone=form_data['phone'],
      street_address=form_data['address'],
      zip_code=form_data['zipcode'],
      category=form_data['category'],
    )

    return redirect('/login/')

  else:
    return render(request, 'tradefood/register.html')

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      return render(request, 'tradefood/login.html', {'error': 'Invalid login'})

  else:
    return render(request, 'tradefood/login.html')