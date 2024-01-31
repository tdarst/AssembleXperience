import unittest
from . import UT_master

class TestParseAdd(unittest.TestCase):
    
    def __init__(self):
        self.test_vars = UT_master.TestVars()

    # Test ADD, R1, R1, R2
    def test_Given_DR_SR1_SR2_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ADD, 
                                                              operands=[test_vars.TOK_R1,
                                                                        test_vars.TOK_R2, 
                                                                        test_vars.TOK_R3], 
                                                              labels=[])
        
        self.assertTrue(parselib.parse_add(address, tokens, []), '0001001000000010')

    # Test ADD, R1, R1, #1
    def test_Given_DR_SR1_IMM5_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ADD,
                                                        operands=[test_vars.TOK_R1,
                                                                  test_vars.TOK_R2,
                                                                  test_vars.TOK_IMM5_1],
                                                        labels=[])
        
        self.assertTrue(parselib.parse_add(address, tokens, []), '0001001000000001')

    # Test ADD, R1, R1, NUM 
    # where line is at 0x3000 and NUM is resovled at 0x3010
    def test_Given_DR_SR1_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars

        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ADD,
                                                              operands=[test_vars.TOK_R1,
                                                                        test_vars.TOK_R1,
                                                                        test_vars.TOK_LABEL_NUM],
                                                              labels=[test_vars.TOK_LABEL_NUM])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_NUM,
                                                              address=test_vars.ADDRESS_0X3010)
        
        self.assertTrue(parselib.parse_add(address, tokens, label_lookup), '0001001000001000')


        
