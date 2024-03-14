import unittest
from ..Unit_Tests_validlib import Class_TestVars_validlib
from ...Supporting_Libraries import validlib, utils

class TestValidBlkw(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_validlib.TestVars_validlib()

    # Testing
    # NUM .BLKW 0x0 = error_str
    # NUM .BLKW 0 = error_str
    # NUM .BLKW #0 = error_str
    # NUM .BLKW 1234 = error_str
    # NUM .BLKW 0x1F5 = error_str
    # NUM .BLKW 111110101 = error_str
    # NUM .BLKW #501 = error_str    
    def test_Given_wrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_hex_0],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_bin_0],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_hash_0],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table4 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.invalid_value],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table5 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_hex_past_upper_limit],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table6 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_bin_past_upper_limit],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table7 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands = [test_vars.fake_blkw_hash_past_upper_limit],
            labels = [test_vars.TOK_LABEL_NUM]
        )

        self.assertEqual(validlib.valid_blkw(symbol_table,  []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_hex_0, test_vars.range_blkw))
        self.assertEqual(validlib.valid_blkw(symbol_table2, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_bin_0, test_vars.range_blkw))
        self.assertEqual(validlib.valid_blkw(symbol_table3, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_hash_0, test_vars.range_blkw))
        self.assertEqual(validlib.valid_blkw(symbol_table4, []), validlib.ERROR_OPERAND_TYPE_STR(test_vars.invalid_value))
        self.assertEqual(validlib.valid_blkw(symbol_table5, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_hex_past_upper_limit, test_vars.range_blkw))
        self.assertEqual(validlib.valid_blkw(symbol_table6, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_bin_past_upper_limit, test_vars.range_blkw))
        self.assertEqual(validlib.valid_blkw(symbol_table7, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(test_vars.fake_blkw_hash_past_upper_limit, test_vars.range_blkw))

    # TEST
    # 2 operands = error_str
    def test_Given_TooManyOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands=[test_vars.HEX_VAL_0X20, test_vars.TOK_R1],
            labels = []
        )

        self.assertEqual(validlib.valid_blkw(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS]))) 

    # TEST
    # 0 operand = error_str
    def test_Given_TooFewOperands_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_BLKW,
            operands=[],
            labels = []
        )

        self.assertEqual(validlib.valid_blkw(symbol_table, []), validlib.ERROR_OPERAND_LENGTH_STR(1, len(symbol_table[utils.KEY_OPERANDS])))