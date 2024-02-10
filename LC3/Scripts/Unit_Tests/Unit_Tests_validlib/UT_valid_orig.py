import unittest
from ..Unit_Tests_utils import Class_TestVars_utils
from ...Supporting_Libraries import validlib

class TestValidOrig(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Testing
    # .ORIG #1 = error_str
    # .ORIG R1 = error_str
    # .ORIG LOOP = error_str
    def test_Given_wrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ORIG,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ORIG,
            operands = [test_vars.TOK_R1],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ORIG,
            operands = [test_vars.TOK_LABEL_LOOP],
            labels = [test_vars.TOK_LABEL_LOOP]
        )

        self.assertEqual(validlib.valid_orig(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_orig(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_R1))
        self.assertEqual(validlib.valid_orig(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))