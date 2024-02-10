import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib

class TestValidAnd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Testing
    # AND #1 R1 R2 = error_str
    # AND 0x20 R1 R2 = error_str
    # AND LOOP R1 R2 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands = [test_vars.TOK_IMM5_1, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands = [test_vars.HEX_VAL_0X20, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands = [test_vars.TOK_LABEL_LOOP, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )

        self.assertEqual(validlib.valid_and(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_and(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_and(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # AND R1 #1 R2 = error_str
    # AND R1 0x20 R2 = error_str
    # AND R1 LOOP R2 = error_str
    def test_Given_WrongOP2_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands=[test_vars.TOK_R1, test_vars.TOK_IMM5_1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands=[test_vars.TOK_R1, test_vars.HEX_VAL_0X20, test_vars.TOK_R2],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP, test_vars.TOK_R2],
            labels = []
        )

        self.assertEqual(validlib.valid_and(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_and(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_and(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # AND R1 R1 LOOP = error_str
    def test_Given_WrongOP3_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_AND,
            operands=[test_vars.TOK_R1, test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_and(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))