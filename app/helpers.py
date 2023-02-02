from django.core.exceptions import ValidationError
from decimal import Decimal


class Asset:
    """An Asset represent financial asset e.g money"""

    def __init__(self, amount: float, currency: str):
        # input parameters are the asset amount.value and the asset currency or name
        self.amount = Decimal(amount)
        self.currency = currency

    def asset_isvalid_currency(self, asset):
        ''' checks that the asset (the only argument to the method is an asset and the same currency as the instance caller)'''
        if not self.is_asset(asset):
            raise AttributeError(f"{self.__class__.__name__} can not be added to {type(asset)}")
        if not self.is_same_currency(asset):
            raise AttributeError(f"Can not carry out operation on {self.__class__.__name__} of different currencies unit")

    def valid_factor(self, factor):
        ''' checks that the factor to be used for mathematical operation with the asset is a float or an int'''
        if isinstance(factor, (int, float)):
            return True
        return False

    def __bool__(self):
        return bool(self.amount)

    def __eq__(self, asset) -> bool:
        Asset.is_asset(asset)
        self.asset_isvalid_currency(asset)
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

    def __str__(self):
        return f"Asset({self.amount}, {self.currency})"

    def __repr__(self):
        return f'Asset({self.amount}, {self.currency})>'

