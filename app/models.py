from ast import operator
from django.core.exceptions import ValidationError
from django.db import models
from decimal import Decimal


# Create your models here.
class Asset():
    def __init__(self, amount: float, currency: str):
        self.amount = Decimal(amount)
        self.currency = currency

    def asset_isvalid_currency(self, asset):
        ''' checks that the asset (the only argument to the method is an asset and the same currency as the instance caller)'''
        if not self.is_asset(asset):
            raise AttributeError(f"{self.__class__.__name__} can not be added to {type(asset)}")
        if not self.is_same_currency(asset):
            raise AttributeError(f"Can not add {self.__class__.__name__} of different currencies")

    def valid_factor(self, factor):
        ''' checks that the factor to be used for mathematical operation with the asset is a float or an int'''
        if isinstance(factor, (int, float)):
            return True
        return False

    def __bool__(self):
        return bool(self.amount)

    def __eq__(self, asset) -> bool:
        self.is_asset(asset)
        return self.amount == asset.amount

    def __gt__(self, asset):
        self.asset_isvalid_currency(asset)
        return self.amount > asset.amount

    def __lt__(self, asset):
        self.asset_isvalid_currency(asset)
        return self.amount < asset.amount

    def __ge__(self, asset):
        self.asset_isvalid_currency(asset)
        return self.amount >= asset.amount

    def __le__(self, asset):
        self.asset_isvalid_currency(asset)
        return self.amount <= asset.amount

    def __add__(self, asset):
        self.asset_isvalid_currency(asset)
        result = self.amount + asset.amount
        return self.create_asset(result, self.currency)

    def __sub__(self, asset):
        self.asset_isvalid_currency(asset)
        result = self.amount - asset.amount
        return self.create_asset(result, self.currency)

    def __mul__(self, factor):
        if isinstance(factor, self.__class__):
            self.asset_isvalid_currency(factor)
            result = self.amount * factor.amount
            return self.create_asset(result, self.currency)
        if self.valid_factor(factor):
            result = self.amount * Decimal(factor)
            return self.create_asset(result, self.currency)
        else:
            raise AttributeError(f"Can not multiply {self.__class__.__name__} to {type(factor)}")

    def __floordiv__(self, factor):
        return self.__truediv__(factor)

    def __truediv__(self, factor):
        if isinstance(factor, self.__class__):
            self.asset_isvalid_currency(factor)
            result = self.amount * factor.amount
            return self.create_asset(result, self.currency)
        if self.valid_factor(factor):
            result = self.amount / Decimal(factor)
            return self.create_asset(result, self.currency)

    @classmethod
    def create_asset(cls, amount, currency):
        return cls(amount, currency)

    @classmethod
    def is_asset(cls, obj):
        ''' checks that the obj is an asset '''
        if isinstance(obj, cls):
            return True
        return False

    def is_same_currency(self, asset):
        return self.currency == asset.currency

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.amount}, {self.currency})>'


class AssetField(models.Field):
    ASSET_CLASS = Asset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    def parse_asset(self, asset_data):
        if data_size := len(asset_data) != 2:
            raise ValidationError(f'Lenght of asset data should be 2 (and not {data_size})')
        return Asset(*asset_data)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return self.parse_asset(value)
    
    def get_prep_value(self, value):
        if value is None:
            return None
        amount = value.amount
        currency = value.currency
        return f"({amount},{currency})"

    def get_db_prep_value(self, value, connection, prepared):
        if value is None:
            return None
        if not isinstance(value, self.ASSET_CLASS):
            value = self.parse_asset(value)

        return f"{value.amount},{value.currency}"

    def to_python(self, value):
        if isinstance(value, self.ASSET_CLASS):
            return value
        if value is None:
            return None
        return self.parse_asset(value)
