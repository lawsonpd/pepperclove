# pepperclove

Restaurant food trading app built with Django

## Purpose

When I worked in the food industry, my coworkers and I would occasionally trade food with other restaurants. Instead of eating food from our own restaurant for our "shift meals", we would contact a nearby restaurant and trade a few of our entrees for a few of theirs. This was always a treat, but it was time consuming and in some cases a source of inconvenience for the other restaurants we contacted.

My thought was that if there was a marketplace, so to speak, with listings of restaurants who are interested in making trades, then this could greatly simplify the process and also expand the options available to any one restaurant. In my spare time I built a simple auction-like web app to serve just this purpose.

The essential idea is that a restaurant can use the app to make an offer - e.g. a large pepperoni pizza - and other nearby restaurants can place bids of their own products - e.g. 4 hoagies. When a bid is placed, the offerer gets a text message, and when a bid is accepted by the offerer, the bidder gets a text message. At the end of the "auction", i.e. when a bid is accepted, the contact information of each party is shared with their counterpart so that the actual exchange can be carried out.

## Build
- Django
- Twilio
- Postgresql

## Present/future

Pepperclove was primarily a hobby project for learning and experimenting with new APIs (viz. Twilio programmatic SMS), although I do believe something like it could enjoy some commercial success. For the time being it will remain a project that I occasionally visit to implement new features.

In its current form it really is a MVP; only the bare minimum features were implemented. There were several production-necessary features that should be added.

### @future
#### Location

Currently the app has no way of knowing where a user is, so it shows _all_ available offers. One solution to this would be to use something like Google Location Services to request location permissions from the user. Alternatively, the user could enter their zip code and only see offers within that zip code and, perhaps, adjacent zip codes, but obviously some verification process would be necessary.

#### Other industries and categories

The initial inspiration for this app was restaurants and food trading, but there's no reason businesses in other categories couldn't use a similar service. For instance, if a fitness center grants free gym time to their employees and a nearby yoga studio grants something equivalent to their employees, then conceivably the respective employees could trade their "credits".

#### Auction expiration

Currently auctions don't expire, although they can be revoked or nullified. The solution here wouldn't be too complex, although it may require something like a cron job that can automatically update the database object when a certain duration has elasped.

#### Exposing competing bids

There's no way, as it is, for a bidder to see competing bids. This may have been a design decision when I first conceived of the UI/UX, but it would make sense to make that information available. The app also does _not_ notify a bidder when a competing bid has been made and it doesn't prevent a user from placing more than one bid on an offer. As with some of the ideas above, these wouldn't be difficult to implement, but they aren't at present.

