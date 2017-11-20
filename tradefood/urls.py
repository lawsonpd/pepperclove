from django.conf.urls import url

from . import views

urlpatterns = [
  # extend '/offers/'
  # url(r'^register/$', views.register),
  url(r'^register/$', views.temp_register_unavailable),
  url(r'^login/$', views.login_view),
  url(r'^logout/$', views.logout_view),
  url(r'^$', views.home),
  url(r'^offers/$', views.open_offers),
  url(r'^offers/(?P<offer_pk>\d+)/$', views.offer_details),
  url(r'^bid/(?P<offer_pk>\d+)/$', views.submit_bid),
  url(r'^bids/(?P<bid_pk>\d+)/$', views.bid_details),
  url(r'^my-offers/$', views.my_offers),
  url(r'^my-bids/$', views.my_bids),
  url(r'^trade/$', views.submit_offer),
  url(r'^accept-bid/(?P<bid_pk>\d+)/$', views.accept_bid),
  # for let's encrypt
  url(r'^\.well-known/acme-challenge/Q4uR9oYEZ4l4jFjqhEa_mk6nUkNvtWf2iajClq13GOs/$', views.lets_encrypt),
]
