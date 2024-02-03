import unittest
from . import Class_TestVars_utils
import utils

class TestIntToBin(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test int_to_bin(1) == '1'
    def test_Given_1_Produce_CorrectBinaryString(self):
        test_vars = self.test_vars
        self.assertEqual(utils.int_to_bin(test_vars.int_val_1), '1')

    # Test int_to_bin(2) == '10'
    def test_Given_2_Produce_CorrectBinaryString(self):
        test_vars = self.test_vars
        self.assertEqual(utils.int_to_bin(test_vars.int_val_2), '10')

    # Test int_to_bin(3) == '11'
    def test_Given_3_Produce_CorrectBinaryString(self):
        test_vars = self.test_vars
        self.assertEqual(utils.int_to_bin(test_vars.int_val_3), '11')

    # Test int_to_bin(10) == '1010'
    def test_Given_10_Produce_CorrectBinaryString(self):
        test_vars = self.test_vars
        self.assertEqual(utils.int_to_bin(test_vars.int_val_10), '1010')

    # Test int_to_bin(100) == '1100100'
    def test_Given_100_Produce_CorrectBinaryString(self):
        test_vars = self.test_vars
        self.assertEqual(utils.int_to_bin(test_vars.int_val_100), '1100100')