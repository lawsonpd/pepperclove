from django import forms

from tradefood.models import Offer, Bid, Merchant

# class OfferForm(forms.ModelForm):
#   class Meta:
#     model = Offer
#     fields = ['description', 'retail_value', 'contact_name', 'contact_phone', 'duration']
#     localized_fields = ('retail_value',)

# class BidForm(forms.ModelForm):
#   class Meta:
#     model = Bid
#     fields = ['description', 'retail_value', 'contact_name', 'contact_phone', 'duration']
#     localized_fields = ('retail_value',)

DURATION_CHOICES = (
  (0.5, '30 minutes'),
  (1.0, '1 hour'),
  (2.0, '2 hours'),
  (3.0, '3 hours'),
)

class OfferFormCustom(forms.Form):
  description = forms.CharField(label="Description", max_length=100)
  retail_value = forms.FloatField(label="Retail value", required=False)
  contact_name = forms.CharField(label="Contact name")
  contact_phone = forms.CharField(label="Contact phone")
  duration = forms.ChoiceField(
    label="Expires in",
    widget=forms.Select,
    choices=DURATION_CHOICES,
  )

class BidFormCustom(forms.Form):
  description = forms.CharField(label="Description", max_length=100)
  retail_value = forms.FloatField(label="Retail value", required=False)
  contact_name = forms.CharField(label="Contact name")
  contact_phone = forms.CharField(label="Contact phone")
  duration = forms.ChoiceField(
    label="Expires in",
    widget=forms.Select,
    choices=DURATION_CHOICES,
  )

class MerchantForm(forms.ModelForm):
  class Meta:
    model = Merchant
    fields = ['name', 'email', 'phone', 'category']