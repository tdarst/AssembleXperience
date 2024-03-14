import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestHashToBin(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test hash_to_bin('#1') == '1'
    def test_Given_hash1_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_bin(test_vars.TOK_IMM5_1), '1')

    # Test hash_to_int('2') == '10'
    def test_Given_hash2_Produce_CorrectBinValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_bin(test_vars.TOK_IMM5_2), '10')