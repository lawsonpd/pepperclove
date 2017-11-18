# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.

from tradefood.models import Offer, Bid, Merchant
from tradefood.utilities import is_alive

class OfferTestCase(TestCase):
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
      duration=2.0/24.0,
    )

  def test_bid_time_details(self):
    test_bid = Bid.objects.create(
      description='21 inch 1-topping pizza',
      merchant=Merchant.objects.get(name='Test Merchant 2'),
      retail_value=21.50,
      contact_name='Nancy',
      contact_phone='615-333-6666',
      offer=Offer.objects.get(description='1 dozen chocolate chip cookies'),
    )

    test_offer = Offer.objects.get(description='1 dozen chocolate chip cookies')

    assert is_alive(test_bid)
    assert is_alive(test_offer)

  def test_expiration(self):
    c = Client()

    test_offer_data = {
      'description': 'chicken',
      'merchant': Merchant.objects.get(username='hattieb-charlotte'),
      'retail_value': '0.0',
      'contact_name': 'John',
      'contact_phone': '615-666-8888',
      'duration': 1.0
    }

    test_submit_offer_res = c.post('/trade/', test_offer_data)

    test_bid_data = {
      'description': 'cookies',
      'merchant': Merchant.objects.get(username='jakesbakes'),
      'retail_value': '0.0',
      'contact_name': 'Tom',
      'contact_phone': '615-999-3333',
      'duration': 0.5
    }

    test_submit_bid_res = c.post('/bid/{0}'.format(test_submit_offer_res), test_bid_data)

    assert True
