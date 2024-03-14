from ..Unit_Tests_parselib import Class_TestVars_parselib
from ...Supporting_Libraries import utils

class TestVars_validlib(Class_TestVars_parselib.TestVars):
    def __init__(self):
        super().__init__()

        self.fake_imm16_hex_32768 = '0x8000'
        self.fake_imm16_bin_32768 = '1000000000000000'
        self.fake_imm16_hash_32768 = "#32768"
        self.invalid_value = '1234'

        self.fake_imm16_hex_neg_32769 = '-0x8001'
        self.fake_imm16_bin_neg_32769 = '1111111111111111'
        self.fake_imm16_hash_neg_32769 = "#-32769"

        self.fake_blkw_hex_0 = '0x0'
        self.fake_blkw_bin_0 = '0'
        self.fake_blkw_hash_0 = '#0'
        self.fake_blkw_hex_past_upper_limit = '#501'
        self.fake_blkw_bin_past_upper_limit = '111110101'
        self.fake_blkw_hash_past_upper_limit = '#501'

        self.fake_stringz_past_upper_limit = '"' + 'a'*501 + '"'
        self.fake_stringz_no_right_quote = '"ASDF'
        self.fake_stringz_no_left_quote = 'ASDF"'

        self.TOK_TRAP_VECTOR_0X22 = 0x22

        self.range_imm16 = utils.IMM16_INT_RANGE
        self.range_blkw = utils.BLKW_INT_RANGE
        self.range_stringz = utils.STRINGZ_INT_RANGE