import unittest
from ..Unit_Tests_utils import Class_TestVars_utils
from ...Supporting_Libraries import validlib

class TestValidExplicitTrap(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Testing
    # HALT #1 = error_str
    # HALT R1 R2 = error_str
    # HALT LOOP = error_str
    def test_Given_AnyNumOfOP_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_HALT,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_HALT,
            operands = [test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_HALT,
            operands = [test_vars.TOK_LABEL_LOOP],
            labels = [test_vars.TOK_LABEL_LOOP]
        )

        self.assertEqual(validlib.valid_explicit_trap(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(0, 1))
        self.assertEqual(validlib.valid_explicit_trap(symbol_table2, []), validlib.ERROR_OPERAND_LENGTH_STR(0, 2))
        self.assertEqual(validlib.valid_explicit_trap(symbol_table3, []), validlib.ERROR_OPERAND_LENGTH_STR(0, 1))