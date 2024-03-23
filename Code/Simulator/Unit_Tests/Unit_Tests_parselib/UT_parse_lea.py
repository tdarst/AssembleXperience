import unittest
from . import Class_TestVars_asemlib
from ...Supporting_Libraries import asemlib

class TestParseLea(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Test
    # x3000 LEA R1 LOOP
    # x3001 LOOP
    def test_Given_LEA_R1_LABEL_Offset_Positive_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LEA, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertEqual(asemlib.asem_lea(address, tokens, label_lookup), '1110001000000000')

    # Test
    # x3000 LEA R1 LOOP
    # x3001 LOOP
    def test_Given_LEA_R1_LABEL_Offset_Negative_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3001
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_LEA, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3000)
        
        self.assertEqual(asemlib.asem_lea(address, tokens, label_lookup), '1110001111111110')