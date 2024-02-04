import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestCalcOffset9(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test calc_offset9('0x3000', '0x3010') == '000010000'
    def test_Given_0x3000_0x3010_Produce_000010000(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_offset9(test_vars.address_0x3000,
                                            test_vars.address_0x3010), '111101111')
        
    # Test calc_offset9('0x3010', '0x3000') == '000001111'
    def test_Given_0x3010_0x3000_Produce_000001111(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_offset9(test_vars.address_0x3010,
                                            test_vars.address_0x3000), '000001111')