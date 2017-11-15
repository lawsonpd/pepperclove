from django.conf.urls import url

from . import views

urlpatterns = [
  # extend '/offers/'
  url(r'^$', views.see_all_offers),
  url(r'^trade/$', views.submit_offer),
]
