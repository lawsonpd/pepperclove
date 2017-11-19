# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from django.utils.timezone import now, timedelta

# Create your tests here.

from tradefood.models import Offer, Bid, Merchant
from tradefood.utilities import is_alive

class OfferTestCase1(TestCase):
  def setUp(self):
    test_user1 = User.objects.create_user('test1', 'test1@email.com', 'testpw')
    test_user2 = User.objects.create_user('test2', 'test2@email.com', 'testpw')

    # Test Merchants (one for test offer, one for test bid)
    test_merch1 = Merchant.objects.create(
      user=test_user1,
      name='Test Merchant 1',
      email='test1@email.com',
      phone='615-111-2222',
    )
    test_merch2 = Merchant.objects.create(
      user=test_user2,
      name='Test Merchant 2',
      email='test2@email.com',
      phone='615-222-3333',
      street_address='1212 Main St.',
      zip_code='34343',
    )

    test_offer = Offer.objects.create(
      description='1 dozen chocolate chip cookies',
      merchant=test_merch1,
      retail_value=18.56,
      contact_name='John',
      contact_phone='615-444-5555',
      expiry=now() + timedelta(2.0/24.0)
    )

  def test_bid_time_details(self):
    test_bid = Bid.objects.create(
      description='21 inch 1-topping pizza',
      merchant=Merchant.objects.get(name='Test Merchant 2'),
      retail_value=21.50,
      contact_name='Nancy',
      contact_phone='615-333-6666',
      offer=Offer.objects.get(description='1 dozen chocolate chip cookies'),
      expiry=now() + timedelta(1.0/24.0)
    )

    test_offer = Offer.objects.get(description='1 dozen chocolate chip cookies')

    assert test_bid.is_alive()
    assert test_offer.is_alive()

  def test_expiration_db_create(self):
    offer_post_date = now()

    test_offer = Offer.objects.create(
      description='chicken',
      merchant=Merchant.objects.get(name='Test Merchant 1'),
      retail_value='0.0',
      contact_name='John',
      contact_phone='615-666-8888',
      date_posted=offer_post_date,
      expiry=offer_post_date + timedelta(1.0/24.0)
    )

    bid_post_date = now() + timedelta(0.25/24.0)

    test_bid = Bid.objects.create(
      description='cookies',
      offer=test_offer,
      merchant=Merchant.objects.get(name='Test Merchant 2'),
      retail_value='0.0',
      contact_name='Tom',
      contact_phone='615-999-3333',
      date_posted=bid_post_date,
      expiry=bid_post_date + timedelta(0.5/24.0)
    )

    assert test_offer.is_alive()
    assert test_bid.is_alive()
    assert test_offer.date_posted + timedelta(1.0/24.0) > test_bid.date_posted + timedelta(0.5/24.0)
    assert test_offer.date_posted + timedelta(1.0/24.0) == test_offer.expiry
    assert (now() + timedelta(0.5/24.0)) - (test_bid.date_posted + timedelta(0.5/24.0)) < timedelta(0.5/24.0)



class OfferTestCase2(TestCase):
  def setUp(self):
    test_user1 = User.objects.create_user('test1', 'test1@email.com', 'testpw')
    test_user2 = User.objects.create_user('test2', 'test2@email.com', 'testpw')

    # Test Merchants (one for test offer, one for test bid)
    test_merch1 = Merchant.objects.create(
      user=test_user1,
      name='Test Merchant 1',
      email='test1@email.com',
      phone='615-111-2222',
    )
    test_merch2 = Merchant.objects.create(
      user=test_user2,
      name='Test Merchant 2',
      email='test2@email.com',
      phone='615-222-3333',
      street_address='1212 Main St.',
      zip_code='34343',
    )

    test_offer = Offer.objects.create(
      description='1 dozen chocolate chip cookies',
      merchant=test_merch1,
      retail_value=18.56,
      contact_name='John',
      contact_phone='615-444-5555',
      expiry=now() + timedelta(2.0/24.0)
    )

  def test_expiration_POST(self):
    c = Client()

    test_offer_data = {
      'description': 'chicken',
      'merchant': Merchant.objects.get(name='Test Merchant 1'),
      'retail_value': '0.0',
      'contact_name': 'John',
      'contact_phone': '615-666-8888',
      'expiry': now() + timedelta(1.0/24.0)
    }

    test_submit_offer_res = c.post('/trade/', test_offer_data)

    test_bid_data = {
      'description': 'cookies',
      'offer': test_offer_object,
      'merchant': Merchant.objects.get(name='Test Merchant 2'),
      'retail_value': '0.0',
      'contact_name': 'Tom',
      'contact_phone': '615-999-3333',
      'expiry': now() + timedelta(0.5/24.0)
    }

    test_submit_bid_res = c.post('/bid/{0}'.format(test_submit_offer_res), test_bid_data)

    test_offer = Offer.objects.get(description='chicken')
    test_bid = Bid.objects.get(description='cookies')

    assert test_offer.is_alive()
    assert test_bid.is_alive()
    assert test_offer.date_posted + timedelta(test_offer.duration) > test_bid.date_posted + timedelta(test_bid.duration)
    assert test_offer.date_posted + timedelta(test_offer.duration) == test_offer.expiry
    assert (now() + timedelta(0.5/24.0)) - (test_bid.date_posted + timedelta(test_bid.duration)) < timedelta(0.5/24.0)
