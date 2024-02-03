import unittest
import Class_TestVars
import parselib

class TestParseAnd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars.TestVars()

    # Test 
    # AND, R1, R1, R2
    def test_Given_DR_SR1_SR2_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_AND, 
                                                              operands=[test_vars.TOK_R1,
                                                                        test_vars.TOK_R1, 
                                                                        test_vars.TOK_R2], 
                                                              labels=[])
        
        self.assertEqual(parselib.parse_add(address, tokens, []), '0101001001000010')

    # Test 
    # AND, R1, R1, #1
    def test_Given_DR_SR1_IMM5_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_AND,
                                                        operands=[test_vars.TOK_R1,
                                                                  test_vars.TOK_R2,
                                                                  test_vars.TOK_IMM5_1],
                                                        labels=[])
        
        self.assertEqual(parselib.parse_add(address, tokens, []), '0101001010100001')