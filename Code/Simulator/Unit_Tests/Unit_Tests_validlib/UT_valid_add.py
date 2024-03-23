import unittest
from ..Unit_Tests_asemlib import Class_TestVars_asemlib
from ...Supporting_Libraries import validlib, utils

class TestValidAdd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_asemlib.TestVars()

    # Testing
    # ADD #1 R1 R2 = error_str
    # ADD 0x20 R1 R2 = error_str
    # ADD LOOP R1 R2 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands = [test_vars.TOK_IMM5_1, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands = [test_vars.HEX_VAL_0X20, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands = [test_vars.TOK_LABEL_LOOP, test_vars.TOK_R1, test_vars.TOK_R2],
            labels = []
        )

        self.assertEqual(validlib.valid_add(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_add(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_add(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # ADD R1 #1 R2 = error_str
    # ADD R1 0x20 R2 = error_str
    # ADD R1 LOOP R2 = error_str
    def test_Given_WrongOP2_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.TOK_IMM5_1, test_vars.TOK_R2],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.HEX_VAL_0X20, test_vars.TOK_R2],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP, test_vars.TOK_R2],
            labels = []
        )

        self.assertEqual(validlib.valid_add(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_add(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_add(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # ADD R1 R1 LOOP = error_str
    def test_Given_WrongOP3_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_add(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.TOK_R1, test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_add(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(3, len(symbol_table[utils.KEY_OPERANDS]))) 

    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ADD,
            operands=[test_vars.TOK_R1, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_add(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(3, len(symbol_table[utils.KEY_OPERANDS])))