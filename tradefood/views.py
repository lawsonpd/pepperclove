# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist

from django.utils.timezone import timedelta, now

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tradefood.forms import OfferFormCustom, BidFormCustom, EmailSignupForm
from tradefood.models import Merchant, Offer, Bid, EmailSubscriber
from tradefood.utilities import notify_offerer, notify_bidder

# Create your views here.

@require_http_methods(['GET'])
def lets_encrypt(request):
  return HttpResponse('PkIk0KnC0ebCsF6d4QBaRnFXKstP4t7h7pynlrj860k.LmpInhVWEg6vB1yJk-b8Bd8-yc7wkfxPeiMJwAVbZcQ')

def how_it_works(request):
  return render(request, 'tradefood/info/how_it_works.html')

# Registration temp. unavailable until ready to really launch.
#
@require_http_methods(['GET', 'POST'])
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

    return redirect(reverse('tradefood:login'))

  else:
    return render(request, 'tradefood/auth/register.html')

@require_http_methods(['GET', 'POST'])
def temp_register_unavailable(request):
  if request.method == 'POST':
    form = EmailSignupForm(request.POST)
    if form.is_valid():
      subscriber_info = form.cleaned_data
      subscriber = EmailSubscriber.objects.create(
        name=subscriber_info['name'],
        email=subscriber_info['email']
      )

      # What if they don't enter a name? (Is is required by default?)
      return render(request, 'tradefood/auth/email_signup_success.html', {'name': subscriber_info['name']})
  else:
    form = EmailSignupForm()
    return render(request, 'tradefood/auth/register_unavailable.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect(reverse('tradefood:home'))
    else:
      return render(request, 'tradefood/auth/login.html', {'error_message': 'Invalid login'})

  else:
    return render(request, 'tradefood/auth/login.html')

def logout_view(request):
  logout(request)
  return redirect(reverse('tradefood:home'))

def home(request):
  return render(request, 'tradefood/home.html')

@login_required()
def open_offers(request):
  u = User.objects.get(username=request.user)
  merch = Merchant.objects.get(user=u)
  # offers = Offer.objects.exclude(expiry__lte=now())

  offers = Offer.objects.filter(
    expiry__gt=now(),
    bid_accepted=False
  ).exclude(
    merchant=merch
  )

  return render(request, 'tradefood/offers/offers.html', {'offers': offers})

@login_required()
def submit_bid(request, offer_pk):
  if request.method == 'POST':
    form = BidFormCustom(request.POST)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      merch = Merchant.objects.get(user=u)

      this_offer = Offer.objects.get(pk=offer_pk)

      if this_offer.merchant == merch:
        return render(request, 'tradefood/offer.html', {'error_message': 'Cannot bid on your own order.'})

      form_data = form.cleaned_data
      time_post = now()
      bid_expiry = time_post + timedelta(float(form_data['duration'])/24.0)

      # needed since value can't be null
      rv = form_data['retail_value'] or None

      bid = Bid.objects.create(
        description=form_data['description'],
        merchant=merch,
        offer=this_offer,
        retail_value=rv,
        contact_name=form_data['contact_name'],
        contact_phone=form_data['contact_phone'],
        date_posted=time_post,
        expiry=bid_expiry,
        sms_notifs=form_data['receive_sms_notifications']
      )

      # send SMS notification to offer contact
      if this_offer.sms_notifs: notify_offerer(this_offer)

      return redirect('/my-bids/')
  else:
    this_offer = Offer.objects.get(pk=offer_pk)
    form = BidFormCustom()

    return render(
      request,
      'tradefood/bids/place_bid.html',
      {
       'form': form,
       'offer_pk': offer_pk,
       'description': this_offer.description,
       'merchant': this_offer.merchant.name,
       # 'retail_value': this_offer.retail_value,
       # 'num_bids': this_offer.bids.all().count()
      }
    )

@login_required()
def submit_offer(request):
  if request.method == 'POST':
    form = OfferFormCustom(request.POST)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      merch = Merchant.objects.get(user=u)

      form_data = form.cleaned_data
      time_post = now()
      duration = timedelta(float(form_data['duration'])/24.0)
      offer_expiry = time_post + duration

      # needed since value can't be null
      rv = form_data['retail_value'] or None

      offer = Offer.objects.create(
        description=form_data['description'],
        merchant=merch,
        retail_value=rv,
        contact_name=form_data['contact_name'],
        contact_phone=form_data['contact_phone'],
        date_posted=time_post,
        expiry=offer_expiry,
        sms_notifs=form_data['receive_sms_notifications']
      )

      return redirect('/my-offers/')
  else:
    form = OfferFormCustom()
  return render(request, 'tradefood/offers/trade.html', {'form': form})

@login_required()
def my_bids(request):
  u = User.objects.get(username=request.user)
  merch = Merchant.objects.get(user=u)

  # get bids from today
  bids = merch.bids.filter(
    date_posted__date=now().date()
  ).order_by(
    '-date_posted'
  )

  # e = [is_alive(bid) for bid in bids]
  # alive_bids = [bid for bid in bids if bid.is_alive()]

  # return render(request, 'tradefood/bids/my_bids.html', {'bid_data': zip(bids, e)})
  return render(request, 'tradefood/bids/my_bids.html', {'bids': bids})

@login_required()
def my_offers(request):
  u = User.objects.get(username=request.user)
  merch = Merchant.objects.get(user=u)

  offers = merch.offers.filter(
    date_posted__date=now().date(),
  ).order_by(
    '-date_posted'
  )

  # e = [is_alive(offer) for offer in offers]
  # alive_offers = [offer for offer in offers if offer.is_alive()]

  # return render(request, 'tradefood/bids/my_offers.html', {'offer_data': zip(offers, e)})
  return render(request, 'tradefood/offers/my_offers.html', {'offers': offers})

@login_required()
def bid_details(request, bid_pk):
  u = User.objects.get(username=request.user)
  merch = Merchant.objects.get(user=u)

  bid = Bid.objects.get(pk=bid_pk)

  if bid.offer.merchant == merch:
    return render(request, 'tradefood/bids/bid-offer_owner.html', {'bid': bid, 'owns_offer': True})
  elif bid.merchant == merch:
    return render(request, 'tradefood/bids/bid-bid_owner.html', {'bid': bid, 'owns_bid': True})
  else:
    return render(request, 'tradefood/forbidden.html')

@login_required()
def offer_details(request, offer_pk):
  if request.method == 'GET':
    u = User.objects.get(username=request.user)
    merch = Merchant.objects.get(user=u)

    this_offer = get_object_or_404(Offer, pk=offer_pk)
    try:
      # check whether merch has already bid on this offer
      existing_bid = Bid.objects.get(
        offer=this_offer,
        merchant=merch
      )
    except ObjectDoesNotExist:
      existing_bid = None

    try: 
      winning_bid = this_offer.bids.get(accepted=True)
    except ObjectDoesNotExist:
      winning_bid = None

    payload = {
      'offer': this_offer,
      'winning_bid': winning_bid,
      'existing_bid': existing_bid
    }

    if this_offer.merchant == merch:
      bids = this_offer.bids.all()
      payload['bids'] = bids
      payload['offer_owner'] = True
    else:
      payload['offer_owner'] = False

    return render(request, 'tradefood/offers/offer.html', payload)

@login_required()
def accept_bid(request, bid_pk):
  if request.method == 'POST':
    u = User.objects.get(username=request.user)
    merch = Merchant.objects.get(user=u)

    bid = Bid.objects.get(pk=bid_pk)
    this_offer = bid.offer

    # prevent post requests from other merchants
    if this_offer.merchant != merch:
      return render(request, 'tradefood/forbidden.html')

    if bid.accepted:
      return redirect('/my-offers/', {error_message: 'Bid already accepted.'})

    this_offer.bid_accepted = True
    this_offer.save()

    bid.accepted = True
    bid.save()

    if bid.sms_notifs: notify_bidder(bid)

    return render(
      request,
      'tradefood/bids/bid_accepted.html',
      {
        'offer_desc': this_offer.description,
        'bid_desc': bid.description,
        'bidding_merchant': bid.merchant.name,
        'bid_contact_name': bid.contact_name,
        'bid_contact_phone': bid.contact_phone,
      }
    )
