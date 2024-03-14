import unittest
from . import Class_TestVars_parselib
from ...Supporting_Libraries import parselib

class TestParseLdr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test 
    # LDR, R1, R2, #2
    def test_Given_LDR_DR_SR1_IMM5_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LDR, 
                                                              operands=[test_vars.TOK_R1,
                                                                        test_vars.TOK_R2, 
                                                                        test_vars.TOK_IMM5_2], 
                                                              labels=[])
        
        self.assertEqual(parselib.parse_ldr(address, tokens, []), '0110001010000010')

    # Test 
    # LDR, R1, R2, 0x05
    def test_Given_LDR_DR_SR1_OFFSET6_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LDR, 
                                                              operands=[test_vars.TOK_R1,
                                                                        test_vars.TOK_R2, 
                                                                        test_vars.HEX_VAL_0X5], 
                                                              labels=[])
        
        self.assertEqual(parselib.parse_ldr(address, tokens, []), '0110001010000101')