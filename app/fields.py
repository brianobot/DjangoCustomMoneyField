from django.db import models
from django.forms import ValidationError
from .helpers import Asset


class AssetField(models.Field):
    # used as a class attribute so that it can be easily
    # replaced with other implementation of asset class
    ASSET_CLASS = Asset

    description = "Field to store Asset Instances"

    def __init__(self, *args, **kwargs):
        self.max_length = kwargs.get('max_length')
        self.default_currency = kwargs.get('default_currency', 'naira')
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(25)'

    def parse_asset(self, asset_str):
        """takes a string of 2 items seperated by comma and return an instance of the Asset class"""

        data = asset_str.split(',')
        if len(data) != 2:
            raise ValidationError("Length of asset string must be equal to 2, not ", len(data))
        return Asset(*data)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value

        return self.parse_asset(value)

    def to_python(self, value):
        if isinstance(value, self.ASSET_CLASS):
            return value

        if value is None:
            return value

        return self.parse_asset(value)    
    
    def get_prep_value(self, value):
        if value is None:
            return value

        amount, currency = getattr(value, 'amount', 0), getattr(value, 'currency', self.default_currency)
        return f"{amount},{currency}"

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value 
        
