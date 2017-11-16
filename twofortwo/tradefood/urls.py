from django.conf.urls import url

from . import views

urlpatterns = [
  # extend '/offers/'
  url(r'^register/$', views.register),
  url(r'^login/$', views.login_view),
  url(r'^$', views.root_redirect),
  url(r'^offers/$', views.all_offers),
  url(r'^trade/$', views.submit_offer),
  url(r'^bid/(?P<offer_pk>\d+)/$', views.submit_bid),
]
