# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.utils.timezone import timedelta, now

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from tradefood.forms import *
from tradefood.models import Merchant, Offer, Bid

# Create your views here.

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
      name=form_data['name'],
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
      return redirect('/offers/')
    else:
      return render(request, 'tradefood/login.html', {'error': 'Invalid login'})

  else:
    return render(request, 'tradefood/login.html')

def root_redirect(request):
  return redirect('/offers/')

@login_required(login_url='/login/')
def all_offers(request):
  offers = Offer.objects.filter(expiry__gt=now())
  return render(request, 'tradefood/offers.html', {'offers': offers})

@login_required(login_url='/login/')
def submit_offer(request):
  if request.method == 'POST':
    form = OfferForm(request.POST)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      merch = Merchant.objects.get(user=u)

      form_data = form.cleaned_data
      offer_expiry = now() + timedelta(form_data['duration']/24.0)

      offer = Offer.objects.create(
        description=form_data['description'],
        merchant=merch,
        retail_value=form_data['retail_value'],
        contact_name=form_data['contact_name'],
        contact_phone=form_data['contact_phone'],
        duration=form_data['duration'],
        expiry=offer_expiry,
      )

      return redirect('/offers/')
  else:
    form = OfferForm()
  return render(request, 'tradefood/trade.html', {'form': form})

@login_required(login_url='/login/')
def submit_bid(request, offer_pk):
  if request.method == 'POST':
    form = BidForm(request.POST)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      # should check here that merch placing a bid is the same that made the original offer
      merch = Merchant.objects.get(user=u)

      this_offer = Offer.objects.get(pk=offer_pk)

      form_data = form.cleaned_data
      bid_expiry = now() + timedelta(form_data['duration']/24.0)

      bid = Bid.objects.create(
        description=form_data['description'],
        merchant=merch,
        offer=this_offer,
        retail_value=form_data['retail_value'],
        contact_name=form_data['contact_name'],
        contact_phone=form_data['contact_phone'],
        duration=form_data['duration'],
        expiry=bid_expiry,
      )

      return redirect('/offers/')
  else:
    this_offer = Offer.objects.get(pk=offer_pk)
    form = BidForm()
    return render(
      request,
      'tradefood/bid.html',
      {
       'form': form,
       'offer_pk': offer_pk,
       'description': this_offer.description,
       'merchant': this_offer.merchant.name
      }
    )