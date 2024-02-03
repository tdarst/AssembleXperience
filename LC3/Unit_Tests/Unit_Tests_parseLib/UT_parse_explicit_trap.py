import unittest
from . import Class_TestVars_parselib
import parselib

class TestParseExplicitTrap(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test
    # GETC
    def test_Given_GETC_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_GETC, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100000')

    # Test
    # OUT
    def test_Given_OUT_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_OUT, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100001')

    # Test
    # PUTS
    def test_Given_PUTS_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_PUTS, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100010')

    # Test
    # IN
    def test_Given_IN_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_IN, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100011')

    # Test
    # PUTSP
    def test_Given_PUTSP_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_PUTSP, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100100')

    # Test
    # HALT
    def test_Given_HALT_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_HALT, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_explicit_trap(address, tokens, []), '1111000000100101')