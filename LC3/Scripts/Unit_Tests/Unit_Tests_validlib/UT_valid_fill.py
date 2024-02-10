import unittest
from ..Unit_Tests_validlib import Class_TestVars_validlib
from ...Supporting_Libraries import validlib

class TestValidFill(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_validlib.TestVars_validlib()

    # Testing
    # NUM .FILL 0x8000 = error_str
    # NUM .FILL 1000000000000000 = error_str
    # NUM .FILL #32768 = error_str
    # NUM .FILL 1234 = error_str
    # NUM .FILL -0x8001 = error_str
    # NUM .FILL 10000000000000001 = error_str
    # NUM .FILL #-32769 = error_str    
    def test_Given_wrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_hex_32768],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_bin_32768],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_hash_32768],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table4 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.invalid_value],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table5 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_hex_neg_32769],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table6 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_bin_neg_32769],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table7 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_imm16_hash_neg_32769],
            labels = [test_vars.TOK_LABEL_NUM]
        )

        self.assertEqual(validlib.valid_fill(symbol_table, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_hex_32768, test_vars.range_imm16))
        self.assertEqual(validlib.valid_fill(symbol_table2, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_bin_32768, test_vars.range_imm16))
        self.assertEqual(validlib.valid_fill(symbol_table3, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_hash_32768, test_vars.range_imm16))
        self.assertEqual(validlib.valid_fill(symbol_table4, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.invalid_value))
        self.assertEqual(validlib.valid_fill(symbol_table5, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_hex_neg_32769, test_vars.range_imm16))
        self.assertEqual(validlib.valid_fill(symbol_table6, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_bin_neg_32769, test_vars.range_imm16))
        self.assertEqual(validlib.valid_fill(symbol_table7, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_imm16_hash_neg_32769, test_vars.range_imm16))