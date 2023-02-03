from django.test import TestCase
from .helpers import Asset
from .fields import AssetField


# Create your tests here.
class TestAssetClass(TestCase):
    def test_asset_obj_instantiation(self):
        asset_one = Asset(3.142, 'Naira')
        asset_two = Asset(3.142, 'Dollars')
        asset_three = Asset(3.142, 'Cedes')
        self.assertTrue(asset_one)
        self.assertTrue(asset_two)
        self.assertTrue(asset_three)

    def test_bool_on_asset_obj(self):
        empty_asset_f = Asset(0.0, 'Naira')
        empty_asset_i = Asset(0, 'Dollars')
        self.assertFalse(bool(empty_asset_f))
        self.assertFalse(bool(empty_asset_i))

    def test_equality_on_assets(self):
        one_bitcoin = Asset(1, 'Bitcoin')
        one_ether = Asset(1, 'Ethereum')
        another_one_bitcoin = Asset(1, 'Bitcoin')
        self.assertEqual(one_bitcoin, another_one_bitcoin)
        with self.assertRaises(Exception) as context:
            one_bitcoin == one_ether

        with self.assertRaises(Exception) as context:
            one_bitcoin == (1, 'bitcoin')

    def test_comparism_on_assets(self):
        one_bitcoin = Asset(1, 'Bitcoin')
        two_bitcoin = Asset(2, 'Bitcoin')
        another_one_bitcoin = Asset(1.0, 'Bitcoin')
        self.assertTrue(two_bitcoin > one_bitcoin)
        self.assertTrue(one_bitcoin < two_bitcoin)
        self.assertTrue(one_bitcoin <= another_one_bitcoin)
        self.assertTrue(two_bitcoin >= another_one_bitcoin)

    def test_addition_of_assets(self):
        one_ether = Asset(1, 'Ethereum')
        nine_ether = Asset(9.0, 'Ethereum')
        ten_ether = one_ether + nine_ether
        self.assertTrue(ten_ether.amount == 10)
    
    def test_subtraction_on_assets(self):
        one_ether = Asset(1, 'Ethereum')
        nine_ether = Asset(9.0, 'Ethereum')
        eight_ether = nine_ether - one_ether 
        self.assertTrue(eight_ether.amount == 8)

    def test_multiplication_of_asset(self):
        five_stones = Asset(5, 'Stones')
        two_stones = Asset(2, 'Stones')
        self.assertTrue(five_stones * 2 == Asset(10, 'Stones'))
        self.assertTrue(five_stones * two_stones == Asset(10, 'Stones'))
        with self.assertRaises(Exception) as context:
            five_stones * complex(1)

    def test_division_of_asset(self):
        six_putas = Asset(6, 'Putas')
        two_putas = Asset(2, 'Putas')
        self.assertTrue((six_putas/3) == Asset.create_asset(2.0, 'Putas'))
        self.assertTrue((six_putas//3) == Asset.create_asset(2, 'Putas'))
        self.assertTrue(six_putas/two_putas == Asset.create_asset(3.0, 'Putas'))
        self.assertTrue(six_putas//two_putas == Asset.create_asset(3, 'Putas'))

    def test_create_asset_classmethod(self):
        test_asset = Asset.create_asset(3, 'Dinaris')
        self.assertTrue(test_asset)
        self.assertTrue(isinstance(test_asset, Asset))
        self.assertTrue(test_asset.amount == 3)
        self.assertTrue(test_asset.currency == 'Dinaris')

    def test_is_asset_classmethod(self):
        asset = Asset.create_asset(3, 'Nintobras')
        non_asset = (2, 'FUllnery')
        self.assertTrue(Asset.is_asset(asset))
        self.assertFalse(Asset.is_asset(non_asset))

    def test_is_same_currency_method(self):
        one_dollar = Asset(1, 'Dollars')
        two_dollar = Asset(2, 'Dollars')
        six_dols = Asset(6, 'Dolsdar')
        self.assertTrue(one_dollar.is_same_currency(two_dollar))
        self.assertFalse(one_dollar.is_same_currency(six_dols))

    def test_str_and_repr_method(self):
        asset = Asset(2, 'Naira')
        self.assertTrue(str(asset) == "Asset(2.0, Naira)")
        self.assertTrue(repr(asset) == "<Asset(2.0, Naira)>")


class TestAssetField(TestCase):
    ...