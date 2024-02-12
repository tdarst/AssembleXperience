import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib, utils

class TestValidLdi(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Testing
    # LDI #1 LOOP = error_str
    # LDI 0x20 LOOP = error_str
    # LDI LOOP LOOP = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.TOK_IMM5_1, test_vars.TOK_LABEL_LOOP],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.HEX_VAL_0X20, test_vars.TOK_LABEL_LOOP],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.TOK_LABEL_LOOP, test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_ldi(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_ldi(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_ldi(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # LDI R1 #1 = error_str
    # LDI R1 0X20 = error_str
    # LDI R1 R1 = error_str
    def test_Given_WrongOP2_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.TOK_R1, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.TOK_R1, test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands = [test_vars.TOK_R1, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_ldi(symbol_table, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_ldi(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_ldi(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_R1))

    # TEST
    # 3 operands
    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP, test_vars.TOK_R2],
            labels = []
        )

        self.assertEqual(validlib.valid_ldi(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(2, len(symbol_table[utils.KEY_OPERANDS]))) 

    # TEST
    # 1 operand
    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDI,
            operands=[test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_ldi(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(2, len(symbol_table[utils.KEY_OPERANDS])))