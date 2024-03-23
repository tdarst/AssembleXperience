import unittest
from . import Class_TestVars_asemlib
from ...Supporting_Libraries import asemlib

class TestParseOrig(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Test
    # .ORIG x3000
    def test_Given_ORIG_0X3000_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_ORIG, 
                                                        operands=[test_vars.ADDRESS_0X3000], 
                                                        labels=[])
        
        self.assertEqual(asemlib.asem_orig(address, tokens, []), '0011000000000000')