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
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(25)'

    def parse_asset(self, asset_str):
        """takes a 2-item tuple and return an instance of the Asset class"""
        print('Asset_str = ', asset_str)
        print('Type of Asset_str = ', type(asset_str))

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
        print('Print value for get_prep_value = ', value)
        if value is None:
            return value

        amount, currency = value.amount, value.currency
        return f"{amount},{currency}"

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value 
        
