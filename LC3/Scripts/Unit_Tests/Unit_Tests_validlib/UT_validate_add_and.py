import unittest
from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import validlib

class TestValidateAddAnd(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_parselib.TestVars()

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

        self.assertEqual(validlib.valid_add_and(symbol_table, []), '#1')
        self.assertEqual(validlib.valid_add_and(symbol_table2, []), '0x20')
        self.assertEqual(validlib.valid_add_and(symbol_table3, []), 'LOOP')

    # Testing 
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

        self.assertEqual(validlib.valid_add_and(symbol_table, []), '#1')
        self.assertEqual(validlib.valid_add_and(symbol_table2, []), '0x20')
        self.assertEqual(validlib.valid_add_and(symbol_table3, []), 'LOOP')


