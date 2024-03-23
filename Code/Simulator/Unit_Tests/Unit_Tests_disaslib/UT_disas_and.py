import unittest
from . import Class_TestVars_disaslib
from ...Supporting_Libraries import disaslib

class TestDisasAnd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_disaslib.TestVars_disaslib()

    # Test 
    # 0101001001000010
    def test_Given_And_Mode_0_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_r2
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, R2")

    # Test
    # 0101001001100001
    def test_Given_And_Mode_1_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")