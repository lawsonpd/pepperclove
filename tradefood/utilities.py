from django.utils.timezone import now, timedelta

from twilio.rest import Client
from twofortwo.settings import TWILIO_SID, TWILIO_AUTH_TOKEN

# check whether offer or bid is still alive
def is_alive(obj):
  time_now = now()
  return obj.date_posted + timedelta(obj.duration) > time_now

# send notification to offerer
def notify_offerer(offer, test=False):
  offer_url = 'http://pepperclove.club/offers/{0}'.format(offer.pk)
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  message = client.message.create(
    offer.contact_phone,
    body="Someone has bid on your offer! Visit {0} for details.".format(offer_url),
    from_="+16156100586")

# send notification to bidder
def notify_bidder(bid):
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)