from django.utils.timezone import now, timedelta

from twilio.rest import Client
from twofortwo.settings import TWILIO_SID, TWILIO_AUTH_TOKEN

# check whether offer or bid is still alive
def is_alive(obj):
  time_now = now()
  return obj.date_posted + timedelta(obj.duration) > time_now

# send notification to offerer when bid is placed
def notify_offerer(offer, test=False):
  if not test:
    offer_url = 'http://pepperclove.club/offers/{0}'.format(offer.pk)
  else:
    offer_url = 'localhost:8000/offers/{0}'.format(offer.pk)
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  message = client.messages.create(
    offer.contact_phone,
    body="Hi, {0}! Someone has bid on your offer! Visit {1} for details.".format(offer.contact_name, offer_url),
    from_="+16156100586")

# send notification to bidder when bid is accepted
def notify_bidder(bid, test=False):
  if not test:
    bid_url = 'http://pepperclove.club/bids/{0}'.format(bid.pk)
  else:
    bid_url = 'localhost:8000/bids/{0}'.format(bid.pk)
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  message = client.messages.create(
    bid.contact_phone,
    body="Hi, {0}! {1} accepted your bid! Visit {2} for details.".format(offer.contact_name, bid.offer.merchant, bid_url),
    from_="+16156100586")