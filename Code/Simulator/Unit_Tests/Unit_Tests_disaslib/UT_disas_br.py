import unittest
from . import Class_TestVars_disaslib
from ...Supporting_Libraries import disaslib

class TestDisasBr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_disaslib.TestVars_disaslib()

    # Test 
    # 0000

    def test_Given_BR_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_r2
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, R2")

    # Test
    # 0101001001100001
    def test_Given_BRn_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRz_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRp_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRnz_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRnp_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRzp_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")
        
    def test_Given_BRnzp_BinString_Produce_Correct_Asm_String(self):
        test_vars = self.test_vars
        bin_string = test_vars.bin_and_r1_r1_hash1
        
        self.assertEqual(disaslib.disas_add(bin_string), "AND R1, R1, #1")