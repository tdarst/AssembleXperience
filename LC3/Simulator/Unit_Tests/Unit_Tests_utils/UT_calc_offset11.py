import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestCalcOffset11(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test calc_offset11('0x3000', '0x3010') == '00000010000'
    def test_Given_0x3000_0x3010_Produce_00000010000(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_offset11(test_vars.address_0x3000,
                                             test_vars.address_0x3010), '11111101111')
        
        # Test calc_offset11('0x3010', '0x3000') == '00000001111'
    def test_Given_0x3010_0x3000_Produce_00000010000(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_offset11(test_vars.address_0x3010,
                                             test_vars.address_0x3000), '00000001111')
        
        #00000001111