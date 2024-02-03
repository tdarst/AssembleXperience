import unittest
from . import Class_TestVars_utils
import utils

class TestIsRegister(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test is_register('R0') == True
    def test_Given_R0_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R0), True)

    # Test is_register('R1') == True
    def test_Given_R1_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R1), True)

    # Test is_register('R2') == True
    def test_Given_R2_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R2), True)

    # Test is_register('R3') == True
    def test_Given_R3_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R3), True)

    # Test is_register('R4') == True
    def test_Given_R4_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R4), True)

    # Test is_register('R5') == True
    def test_Given_R5_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R5), True)

    # Test is_register('R6') == True
    def test_Given_R6_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R6), True)

    # Test is_register('R7') == True
    def test_Given_R7_Produce_True(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R7), True)

    # Test is_register('R8') == False
    def test_Given_R8_Produce_False(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.reg_R8), False)

    # Test is_register('alkajsdflkj') == False
    def test_Given_nonsense_Produce_False(self):
        test_vars = self.test_vars
        self.assertEqual(utils.is_register(test_vars.nonsense), False)