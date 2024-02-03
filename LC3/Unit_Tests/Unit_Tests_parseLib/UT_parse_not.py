import unittest
from . import Class_TestVars_parselib
import parselib

class TestParseNot(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test
    # x3000 NOT R1, R2
    def test_Given_NOT_R1_R2_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_NOT, 
                                                        operands=[test_vars.TOK_R1, test_vars.TOK_R2], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_not(address, tokens, []), '1001001010111111')