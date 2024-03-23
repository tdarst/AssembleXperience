import unittest
from . import Class_TestVars_disaslib
from ...Supporting_Libraries import disaslib

class TestDisasAdd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_disaslib.TestVars_disaslib()

    # Test 
    # 0001001001000010
    def test_Given_Add_BinString_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_add_r1_r1_r2
        
        self.assertEqual(disaslib.disas_add(bin_string), "ADD R1, R1, R2")

    # Test
    # 0001001001100001
    def test_Given_DR_SR1_IMM5_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_add_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "ADD R1, R1, #1")
