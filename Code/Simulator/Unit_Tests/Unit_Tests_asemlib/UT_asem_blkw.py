import unittest
from . import Class_TestVars_asemlib
from ...Supporting_Libraries import asemlib

class TestParseBlkw(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Test
    # NUM .BLKW #2
    def test_Given_BLKW_2_Produce_Correct_Binary_String(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_FILL, 
                                                        operands=[test_vars.TOK_IMM5_2], 
                                                        labels=[test_vars.TOK_LABEL_NUM])
        
        self.assertEqual(asemlib.asem_blkw(address, tokens, []), '0000000000000000\n0000000000000000')