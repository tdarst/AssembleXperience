import unittest
from ..Unit_Tests_utils import Class_TestVars_utils
from ...Supporting_Libraries import validlib, utils

class TestValidSt(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Testing
    # ST #1 LOOP = error_str
    # ST 0x20 LOOP = error_str
    # ST LOOP LOOP = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_IMM5_1, test_vars.TOK_LABEL_LOOP],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.HEX_VAL_0X20, test_vars.TOK_LABEL_LOOP],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_LABEL_LOOP, test_vars.TOK_LABEL_LOOP],
            labels = [test_vars.TOK_LABEL_LOOP]
        )

        self.assertEqual(validlib.valid_st(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_st(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_st(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # ST R1 R1 = error_str
    # ST R1 #1 = error_str
    # ST R1 0X20 = error_str
    # ST R1 NUM
    def test_Given_WrongOP2_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        label_lookup = test_vars.generate_tester_label_lookup(
            test_vars.TOK_LABEL_LOOP,
            test_vars.ADDRESS_0X3000
        )

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_R1, test_vars.TOK_R1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_R1, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_R1, test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table4 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands = [test_vars.TOK_R1, test_vars.TOK_LABEL_NUM],
            labels = [test_vars.TOK_LABEL_NUM]
        )

        self.assertEqual(validlib.valid_st(symbol_table, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_R1))
        self.assertEqual(validlib.valid_st(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_st(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_st(symbol_table4, label_lookup), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_LABEL_NUM))

    # TEST
    # 3 operands = error_str
    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands=[test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP, test_vars.offset6_val_31],
            labels = []
        )

        self.assertEqual(validlib.valid_st(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(2, len(symbol_table[utils.KEY_OPERANDS]))) 

    # TEST
    # 1 operand = error_str
    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_ST,
            operands=[test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_st(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(2, len(symbol_table[utils.KEY_OPERANDS])))