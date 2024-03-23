import unittest
from . import Class_TestVars_asemlib
from ...Supporting_Libraries import asemlib

class TestParseTrap(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Test
    # TRAP 0x20
    def test_Given_TRAP_0X20_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X20], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100000')

    # Test
    # TRAP 0x21
    def test_Given_TRAP_0X21_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X21], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100001')

    # Test
    # TRAP 0x22
    def test_Given_TRAP_0X22_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X22], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100010')

    # Test
    # TRAP 0x23
    def test_Given_TRAP_0X23_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X23], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100011')

    # Test
    # TRAP 0x24
    def test_Given_TRAP_0X24_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X24], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100100')

    # Test
    # TRAP 0x25
    def test_Given_TRAP_0X25_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_TRAP, 
                                                        operands=[test_vars.HEX_VAL_0X25], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_trap(address, tokens, []), '1111000000100101')