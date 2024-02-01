import unittest
import Class_TestVars
import parselib

class TestParseJmp(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars.TestVars()

    # Test
    # jmp R1
    def test_Given_JMP_R1_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_JMP, 
                                                        operands=[test_vars.TOK_R1], 
                                                        labels=[])
        
        self.assertEquals(parselib.parse_jmp(address, tokens, []), '1100000001000000')