import unittest
from ..Unit_Tests_asemlib import Class_TestVars_asemlib
from ...Supporting_Libraries import validlib, utils

class TestValidJsrr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Testing
    # JSRR #1 = error_str
    # JSRR 0x20 = error_str
    # JSRR LOOP = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSRR,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSRR,
            operands = [test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSRR,
            operands = [test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_jsrr(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_jsrr(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_jsrr(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSRR,
            operands=[test_vars.TOK_R1, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_jsrr(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS]))) 

    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JSRR,
            operands=[],
            labels = []
        )

        self.assertEqual(validlib.valid_jsrr(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS])))