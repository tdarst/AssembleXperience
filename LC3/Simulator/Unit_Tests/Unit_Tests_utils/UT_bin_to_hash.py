import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestBinToHash(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test bin_to_hash('1101') == '#11'
    def test_Given_1101_Produce_CorrectHashValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.bin_to_hash(test_vars.bin_1101), '#13')

    # Test bin_to_hash('1') == '1'
    def test_Given_1_Produce_CorrectHashValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.bin_to_hash(test_vars.bin_1), '#1')