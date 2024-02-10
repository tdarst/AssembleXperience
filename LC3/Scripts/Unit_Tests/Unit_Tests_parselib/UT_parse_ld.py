import unittest
from . import Class_TestVars_parselib
from ...Supporting_Libraries import parselib

class TestParseLd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test
    # x3000 LD R1 LOOP
    # x3001 LOOP
    def test_Given_LD_R1_LABEL_Offset_Positive_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LD, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertEqual(parselib.parse_ld(address, tokens, label_lookup), '0010001000000000')

    # Test
    # x3000 LOOP
    # x3001 LD R1 LOOP
    def test_Given_LD_R1_LABEL_Offset_Negative_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3001
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LD, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3000)
        
        self.assertEqual(parselib.parse_ld(address, tokens, label_lookup), '0010001111111110')