# Custom DjangoMoneyField

<img src="https://github.com/brianobot/DjangoCustomMoneyField/actions/workflows/django.yml/badge.svg?branch=master" /> &nbsp; <img src="coverage.svg" />

A Django app that provides a custom model field for handling financial asset object as a single database field,
abstracting the asset name(currency) and value(amount) into a single object (At the python and Database Level).

## Description:
I wish to create a class (object) that represent monetarily value agnosticly, it should encapsulate the asset value and currency in a single python object/database field.

Examples include (Assuming said class is called Asset):
- 1000 naira  = Asset(1000.00 'NGN') 
- 1 US dollar = Asset(1.00, 'USD')
- 0.0005 Bitcoin = Asset(0.0005, 'BTC')

## Installation
To install the app, run the following command:

## Usage
To use the custom model field, you need to import it in your model file and add it as a field to your model.  
```
from custom_money_field.fields import AssetField

class MyModel(models.Model):
    custom_field = AssetField()
```

## Feature:
class should provide an interface to support conversion and mathematical interations between standard current units
  
  
## Contribution
If you would like to contribute to this project, please follow the instructions below:

1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch for your changes
4. Make the necessary changes and commit those changes to the new branch
5. Push the branch to the forked repository
6. Submit a pull request

## License
This project is licensed under the MIT License. For more information, see the LICENSE file.


## Maintainer:
- Brian Obot <brianobot9@gmail.com>
