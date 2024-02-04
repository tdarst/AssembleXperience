import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestCalcTwosComplement(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test calc_twos_complement('1101') == 0011
    def test_Given_1101_Produce_0011(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_twos_complement(test_vars.bin_1101), '0011')

    # Test calc_twos_complement('0011') == 1101
    def test_Given_1101_Produce_0011(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_twos_complement(test_vars.bin_0011), '1101')

    # Test calc_twos_complement('1101') == 0011
    def test_Given_0000_Produce_0000(self):
        test_vars = self.test_vars
        self.assertEqual(utils.calc_twos_complement(test_vars.bin_0000), '0000')