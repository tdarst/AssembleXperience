import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestImm5ToBin(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test hash_to_bin(#5) == '101'
    def test_Given_hash5_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_bin(test_vars.imm5_val_5), '101')

    # Test hash_to_bin(#12) == '1100'
    def test_Given_hash12_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_bin(test_vars.imm5_val_12), '1100')