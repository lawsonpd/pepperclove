from django.urls import path

from . import views

app_name = 'tradefood'
urlpatterns = [
  path('register/', views.register, name='register'),
  # path('register/', views.temp_register_unavailable, name='register-unavail'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('', views.home, name='home'),
  path('offers/', views.open_offers, name='open-offers'),
  path('offers/<int:offer_pk>/', views.offer_details, name='offer-details'),
  path('bid/<int:offer_pk>/', views.submit_bid, name='submit-bid'),
  path('bids/<int:bid_pk>/', views.bid_details, name='bid-details'),
  path('my-offers/', views.my_offers, name='my-offers'),
  path('my-bids/', views.my_bids, name='my-bids'),
  path('trade/', views.submit_offer, name='submit-offer'),
  path('accept-bid/<int:bid_pk>/', views.accept_bid, name='accept-bid'),
  # for let's encrypt
  # path('\.well-known/acme-challenge/Q4uR9oYEZ4l4jFjqhEa_mk6nUkNvtWf2iajClq13GOs/', views.lets_encrypt),
  path('how-it-works/', views.how_it_works, name='how-it-works'),
]
