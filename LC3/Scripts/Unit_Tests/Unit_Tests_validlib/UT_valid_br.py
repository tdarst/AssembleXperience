import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib, utils

class TestValidBr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Testing
    # BR #1 = error_str
    # BR 0x20 = error_str
    # BR R1 = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands = [test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands = [test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_br(symbol_table, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_br(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_br(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_LABEL(test_vars.TOK_R1))

    # TEST
    # 2 operands = error_str
    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands=[test_vars.TOK_LABEL_LOOP, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_br(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS]))) 

    # TEST
    # 0 operands = error_str
    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BR,
            operands=[],
            labels = []
        )

        self.assertEqual(validlib.valid_br(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS])))