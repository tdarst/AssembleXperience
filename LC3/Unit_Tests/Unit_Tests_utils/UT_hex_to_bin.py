import unittest
from . import Class_TestVars_utils
import utils

class TestHexToBin(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test hex_to_bin('0x3000') == '11000000000000'
    def test_Given_0x3000_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hex_to_bin(test_vars.hex_val_0x3000), '11000000000000')

    # Test hex_to_bin('0x005') == '101'
    def test_Given_0x005_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hex_to_bin(test_vars.hex_val_0x005), '101')