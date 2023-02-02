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
        another_one_bitcoin = Asset(1, 'Bitcoin')
        self.assertEqual(one_bitcoin, another_one_bitcoin)

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
        self.assertTrue(five_stones * 2 == Asset(10, 'Stones'))

    
