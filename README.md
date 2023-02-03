# Custom DjangoMoneyField

<img src="https://github.com/brianobot/DjangoCustomMoneyField/actions/workflows/django.yml/badge.svg?branch=master" /> &nbsp; <img src="coverage.svg" />

Custom Django Model Field to store and process a financial asset object as a single database field,
abstracting the asset name(current) and value(amount) into a single object.

## Description:
I wish to create a class (object) that represent monetarily value agnosticly, it should encapsulate the asset value and currency in a single python object/database field.

Examples include (Assuming said class is called Asset):
- 1000 naira  = Asset(1000.00 'NGN') 
- 1 US dollar = Asset(1.00, 'USD')
- 0.0005 Bitcoin = Asset(0.0005, 'BTC')


## Implementation


## Feature:
class should provide an interface to support conversion and mathematical interations between standard current units


## Maintainer:
- Brian Obot <brianobot9@gmail.com>
