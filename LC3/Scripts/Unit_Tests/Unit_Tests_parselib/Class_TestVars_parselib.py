from ...Supporting_Libraries import utils

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

# =============================================================================
# Name: TestVars
# Purpose: Creates variables to be used for testing so that I can reuse them
#          easily and also leaves less floating strings in the unit tests.
#          these are mostly used in parselib unittesting but this class is also
#          inherited by TestVars_utils for use in a few utils unit tests.
# =============================================================================
class TestVars():
    def __init__(self):
        self.ADDRESS_0X3001 = '0x3001'
        self.ADDRESS_0X3000 = '0x3000'
        self.ADDRESS_0X3010 = '0x3010'

        self.HEX_VAL_0X5 = '0x5'
        self.HEX_VAL_0X20 = '0x20'
        self.HEX_VAL_0X21 = '0x21'
        self.HEX_VAL_0X22 = '0x22'
        self.HEX_VAL_0X23 = '0x23'
        self.HEX_VAL_0X24 = '0x24'
        self.HEX_VAL_0X25 = '0x25'
        
        self.TOK_R1 = 'R1'
        self.TOK_R2 = 'R2'
        
        self.TOK_IMM5_1 = '#1'
        self.TOK_IMM5_2 = '#2'

        self.TOK_STRING_ABCD = 'abcd'

        self.TOK_LABEL_LOOP = 'LOOP'
        self.TOK_LABEL_NUM = 'NUM'
        self.TOK_LABEL_STRING = 'STRING'

        self.TOK_ADD = 'ADD'
        self.TOK_AND  = 'AND'
        self.TOK_BR = 'BR'
        self.TOK_BRN = 'BRn'
        self.TOK_BRZ = 'BRz'
        self.TOK_BRP = 'BRp'
        self.TOK_BRNZ = 'BRnz'
        self.TOK_BRNP = 'BRnp'
        self.TOK_BRZP = 'BRzp'
        self.TOK_BRNZP = 'BRnzp'
        self.TOK_JMP = 'JMP'
        self.TOK_JSR = 'JSR'
        self.TOK_JSRR = 'JSRR'
        self.TOK_LD = 'LD'
        self.TOK_LDI = 'LDI'
        self.TOK_LDR = 'LDR'
        self.TOK_LEA = 'LEA'
        self.TOK_NOT = 'NOT'
        self.TOK_RET = 'RET'
        self.TOK_RTI = 'RTI'
        self.TOK_ST = 'ST'
        self.TOK_STI = 'STI'
        self.TOK_STR = 'STR'

        self.TOK_TRAP = 'TRAP'
        self.TOK_GETC = 'GETC'
        self.TOK_OUT = 'OUT'
        self.TOK_PUTS = 'PUTS'
        self.TOK_IN = 'IN'
        self.TOK_PUTSP = 'PUTSP'
        self.TOK_HALT = 'HALT'

        self.TOK_ORIG = '.ORIG'
        self.TOK_FILL = '.FILL'
        self.TOK_BLKW = '.BLKW'
        self.TOK_STRINGZ = '.STRINGZ'

        self.TESTER_LABEL_LOOKUP = {}

    def generate_tester_symbol_table(self, opcode, operands = [], labels = []) -> dict:
        new_symbol_table = {}
        new_symbol_table[KEY_OPCODE] = opcode
        new_symbol_table[KEY_OPERANDS] = operands
        new_symbol_table[KEY_LABELS] = labels
        return new_symbol_table
    
    def generate_tester_label_lookup(self, label, address) -> dict:
        new_label_lookup = {}
        new_label_lookup[label] = address
        return new_label_lookup
