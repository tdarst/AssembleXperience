import unittest
from . import Class_TestVars_utils
import utils

class TestHexToInt(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test hex_to_int('0x3000') == 12288
    def test_Given_0x3000_Produce_CorrectIntValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hex_to_int(test_vars.hex_val_0x3000), 12288)

    # Test hex_to_int('0x005') == 5
    def test_Given_0x005_Produce_CorrectIntValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hex_to_int(test_vars.hex_val_0x005), 5)
