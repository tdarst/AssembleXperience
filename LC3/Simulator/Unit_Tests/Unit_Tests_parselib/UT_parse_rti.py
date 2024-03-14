import unittest
from . import Class_TestVars_parselib
from ...Supporting_Libraries import parselib

class TestParseRti(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Test
    # x3000 NOT R1, R2
    def test_Given_RTI_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_RTI, 
                                                        operands=[], 
                                                        labels=[])
        
        self.assertEqual(parselib.parse_rti(address, tokens, []), '1000000000000000')