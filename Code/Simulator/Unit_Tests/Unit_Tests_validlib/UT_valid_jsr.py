import unittest
from ..Unit_Tests_asemlib import Class_TestVars_asemlib
from ...Supporting_Libraries import validlib, utils

class TestValidJsr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Testing
    # JSR #1 = error_str
    # JSR 0x20 = error_str
    # JSR R1 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSR,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSR,
            operands = [test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSR,
            operands = [test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_jsr(symbol_table, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_jsr(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_jsr(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_R1))

    # TEST
    # 2 operands = error_str
    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSR,
            operands=[test_vars.TOK_LABEL_LOOP, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_jsr(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS]))) 

    # TEST
    # 0 operands = error_str
    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSR,
            operands=[],
            labels = []
        )

        self.assertEqual(validlib.valid_jsr(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS])))