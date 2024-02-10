import unittest
from ..Unit_Tests_validlib import Class_TestVars_validlib
from ...Supporting_Libraries import validlib

class TestValidStringz(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_validlib.TestVars_validlib()

    # Testing
    # NUM .STRINGZ " + 'a'*501 + " = error_str
    # NUM .STRINGZ "ASDF = error_str
    # NUM .STRINGZ ASDF" = error_str
    # NUM .STRINGZ = error_str
    def test_Given_wrongOP1_Produce_CorrectErrorString(self):
        test_vars = self.test_vars

        symbol_table = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_stringz_past_upper_limit],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table2 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_stringz_no_right_quote],
            labels = [test_vars.TOK_LABEL_NUM]
        )
        symbol_table3 = test_vars.generate_tester_symbol_table(
            opcode = test_vars.TOK_FILL,
            operands = [test_vars.fake_stringz_no_left_quote],
            labels = [test_vars.TOK_LABEL_NUM]
        )

        self.assertEqual(validlib.valid_fill(symbol_table, []), validlib.ERROR_OPERAND_VALUE_OUT_OF_RANGE(len(test_vars.fake_stringz_past_upper_limit), test_vars.range_stringz))
        self.assertEqual(validlib.valid_fill(symbol_table2, []), validlib.ERROR_OPERAND_INVALID_STRING_NOT_ENCLOSED)
        self.assertEqual(validlib.valid_fill(symbol_table3, []), validlib.ERROR_OPERAND_INVALID_STRING_NOT_ENCLOSED)