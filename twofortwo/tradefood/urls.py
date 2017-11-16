from django.conf.urls import url

from . import views

urlpatterns = [
  # extend '/offers/'
  url(r'^register/$', views.register),
  url(r'^login/$', views.login_view),
  url(r'^$', views.root_redirect),
  url(r'^offers/$', views.open_offers),
  url(r'^offers/(?P<offer_pk>\d+)/$', views.offer_details),
  url(r'^bid/(?P<offer_pk>\d+)/$', views.submit_bid),
  url(r'^bids/(?P<bid_pk>\d+)/$', views.bid_details),
  url(r'^my-offers/$', views.my_offers),
  url(r'^my-bids/$', views.my_bids),
  url(r'^trade/$', views.submit_offer),
  url(r'^accept-bid/(?P<bid_pk>\d+)/$', views.accept_bid),
]
