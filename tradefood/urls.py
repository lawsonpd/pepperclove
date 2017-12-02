from django.conf.urls import url

from . import views

urlpatterns = [
  # url(r'^register/$', views.register, name='register'),
  url(r'^register/$', views.temp_register_unavailable, name='register-unavail'),
  url(r'^login/$', views.login_view, name='login'),
  url(r'^logout/$', views.logout_view, name='logout'),
  url(r'^$', views.home, name='home'),
  url(r'^offers/$', views.open_offers, name='open-offers'),
  url(r'^offers/(?P<offer_pk>\d+)/$', views.offer_details, name='offer-details'),
  url(r'^bid/(?P<offer_pk>\d+)/$', views.submit_bid, name='submit-bid'),
  url(r'^bids/(?P<bid_pk>\d+)/$', views.bid_details, name='bid-details'),
  url(r'^my-offers/$', views.my_offers, name='my-offers'),
  url(r'^my-bids/$', views.my_bids, name='my-bids'),
  url(r'^trade/$', views.submit_offer, name='submit-offer'),
  url(r'^accept-bid/(?P<bid_pk>\d+)/$', views.accept_bid, name='accept-bid'),
  # for let's encrypt
  # url(r'^\.well-known/acme-challenge/Q4uR9oYEZ4l4jFjqhEa_mk6nUkNvtWf2iajClq13GOs/$', views.lets_encrypt),
  url(r'^how-it-works/$', views.how_it_works, name='how-it-works'),
]
