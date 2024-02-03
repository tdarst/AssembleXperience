import unittest
from . import Class_TestVars_utils
import utils

class TestIsOffset6(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test is_offset6('#5') == True
    def test_Given_Offset6_1_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_offset6(test_vars.offset6_val_5), True)

    # Test is_offset6('#-32') == True
    def test_Given_Offset6_Neg32_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_offset6(test_vars.offset6_val_neg32), True)

    # Test is_offset6('#31') == True
    def test_Given_Offset6_31_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_offset6(test_vars.offset6_val_31), True)

    # Test is_offset6('#32') == False
    def test_Given_Offset6_32_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_offset6(test_vars.fake_offset6_val_32), False)

    # Test is_offset6('#-33') == False
    def test_Given_Offset6_Neg33_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_offset6(test_vars.fake_offset6_val_neg33), False)