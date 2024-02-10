import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib

class TestValidJmp(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

    # Testing
    # JMP #1 = error_str
    # JMP 0x20 = error_str
    # JMP LOOP = error_str
    def test_Given_WrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JMP,
            operands = [test_vars.TOK_IMM5_1],
            labels = []
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JMP,
            operands = [test_vars.HEX_VAL_0X20],
            labels = []
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_JMP,
            operands = [test_vars.TOK_LABEL_LOOP],
            labels = []
        )

        self.assertEqual(validlib.valid_jmp(symbol_table, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_IMM5_1))
        self.assertEqual(validlib.valid_jmp(symbol_table2, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.HEX_VAL_0X20))
        self.assertEqual(validlib.valid_jmp(symbol_table3, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.TOK_LABEL_LOOP))