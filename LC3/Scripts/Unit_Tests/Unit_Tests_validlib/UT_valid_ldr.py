import unittest
from ..Unit_Tests_utils import Class_TestVars_utils
from ...Supporting_Libraries import validlib

class TestValidLdr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Testing
    # LDR #1 R1 #1 = error_str
    # LDR 0x20 R1 #1 = error_str
    # LDR LOOP R1 #1 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_IMM5_1, test_vars.TOK_R1, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.HEX_VAL_0X20, test_vars.TOK_R1, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_LABEL_LOOP, test_vars.TOK_R1, test_vars.TOK_IMM5_1],
            labels = []
        )

        self.assertEqual(validlib.valid_ldr(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_ldr(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_ldr(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # LDR R1 #1 #1 = error_str
    # LDR R1 0X20 #1 = error_str
    # LDR R1 LOOP #1 = error_str
    def test_Given_WrongOP2_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.TOK_IMM5_1, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.HEX_VAL_0X20, test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.TOK_LABEL_LOOP, test_vars.TOK_IMM5_1],
            labels = [test_vars.TOK_LABEL_LOOP]
        )

        self.assertEqual(validlib.valid_ldr(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_ldr(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_ldr(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))

    # Testing
    # LDR R1 R2 #32 = error_str
    # LDR R1 R2 LOOP = error_str
    # LDR R1 R2 R1 = error_str
    def test_Given_WrongOP3_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.TOK_R2, test_vars.fake_offset6_val_32],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.TOK_R2, test_vars.TOK_LABEL_LOOP],
            labels = [test_vars.TOK_LABEL_LOOP]
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_LDR,
            operands = [test_vars.TOK_R1, test_vars.TOK_R2, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_ldr(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.fake_offset6_val_32))
        self.assertEqual(validlib.valid_ldr(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))
        self.assertEqual(validlib.valid_ldr(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_R1))