import unittest
from . import Class_TestVars_parselib
from ...Supporting_Libraries import parselib

class TestParseSt(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test
    # x3000 ST R1 NUM
    # x3001 NUM .FILL 0x3010
    def test_Given_ST_R1_LABEL_Offset_Positive_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ST, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_NUM], 
                                                        labels=[test_vars.TOK_LABEL_NUM])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_NUM,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertEqual(parselib.parse_st(address, tokens, label_lookup), '0011001000000000')

    # Test
    # x3000 NUM .FILL 0x3010
    # x3001 ST R1 NUM
    def test_Given_ST_R1_LABEL_Offset_Negative_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3001
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ST, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_NUM], 
                                                        labels=[test_vars.TOK_LABEL_NUM])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_NUM,
                                                              address=test_vars.ADDRESS_0X3000)
        
        self.assertEqual(parselib.parse_st(address, tokens, label_lookup), '0011001111111110')