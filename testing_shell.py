from django.contrib.auth.models import User

from tradefood.models import Merchant, Bid, Offer



all_users = User.objects.all()

all_offers = Offer.objects.all()

all_bids = Bid.objects.all()
