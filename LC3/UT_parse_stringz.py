import unittest
import Class_TestVars
import parselib

class TestParseStringz(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars.TestVars()

        self.test_string_abcd = "0000000001100001\n0000000001100010\n0000000001100011\n0000000001100100\n0000000000000000"

    # Test
    # STRING .STRINGZ "abcd"
    def test_Given_STRINGZ_abcd_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_STRINGZ, 
                                                        operands=[test_vars.TOK_STRING_ABCD], 
                                                        labels=[test_vars.TOK_LABEL_STRING])
        
        self.assertEqual(parselib.parse_stringz(address, tokens, []), self.test_string_abcd)