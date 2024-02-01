import utils

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS
class TestVars():
    def __init__(self):
        self.ADDRESS_0X3001 = '0x3001'
        self.ADDRESS_0X3000 = '0x3000'
        
        self.TOK_R1 = 'R1'
        self.TOK_R2 = 'R2'
        
        self.TOK_IMM5_1 = '#1'
        self.TOK_IMM5_2 = '#2'

        self.TOK_LABEL_LOOP = 'LOOP'
        self.TOK_LABEL_NUM = 'NUM'

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
