import unittest
from . import Class_TestVars_utils
import utils

class TestIsImm5(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test is_register('#5') == True
    def test_Given_hash5_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.imm5_val_5), True)

    # Test is_register('#-16') == True
    def test_Given_hashNeg16_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.imm5_val_neg16), True)

    # Test is_register('#15') == True
    def test_Given_hash15_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.imm5_val_15), True)

    # Test is_register('#-17') == False
    def test_Given_hashNeg17_Produce_False(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.fake_imm5_neg17), False)

    # Test is_register('#16') == False
    def test_Given_hash16_Produce_False(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.fake_imm5_16), False)

    # Test is_register('alkajsdflkj') == False
    def test_Given_nonsense_Produce_False(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_imm5(test_vars.nonsense), False)