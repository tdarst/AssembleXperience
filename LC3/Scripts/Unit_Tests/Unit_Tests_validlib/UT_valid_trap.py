import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib

class TestValidTrap(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Testing
    # TRAP #1 = error_str
    # TRAP 0x005 = error_str
    # TRAP R1 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_TRAP,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands = [test_vars.HEX_VAL_0X5],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands = [test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_trap(symbol_table, []), validlib.ERROR_OPERAND_INVALID_TRAP_VECTOR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_trap(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_TRAP_VECTOR(test_vars.HEX_VAL_0X5))
        self.assertEqual(validlib.valid_trap(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_TRAP_VECTOR(test_vars.TOK_R1))