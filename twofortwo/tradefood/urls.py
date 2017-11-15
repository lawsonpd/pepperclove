from django.conf.urls import url

from . import views

urlpatterns = [
  # extend '/offers/'
  url(r'^offers/$', views.all_offers),
  url(r'^trade/$', views.submit_offer),
  url(r'^register/$', views.register),
  url(r'^login/$', views.login_view),
]
