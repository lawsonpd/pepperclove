from django.forms import ModelForm

from tradefood.models import Offer, Bid, Merchant

class OfferForm(ModelForm):
  class Meta:
    model = Offer
    fields = ['description', 'retail_value', 'contact_name', 'contact_phone', 'duration']
    localized_fields = ('retail_value',)

class BidForm(ModelForm):
  class Meta:
    model = Bid
    fields = ['description', 'retail_value', 'contact_name', 'contact_phone', 'duration']

class MerchantForm(ModelForm):
  class Meta:
    model = Merchant
    fields = ['name', 'email', 'phone', 'category']