import unittest
from . import UT_parse_add

KEY_OPCODE = 'opcode'
KEY_OPERANDS = 'operands'
KEY_LABELS = 'labels'

class TestVars():
    def __init__(self):
        self.ADDRESS_0X3010 = '0x3010'
        self.ADDRESS_0X3000 = '0X3000'
        
        self.TOK_R1 = 'R1'
        self.TOK_R2 = 'R2'
        
        self.TOK_IMM5_1 = '#1'
        self.TOK_IMM5_2 = '#2'

        self.TOK_LABEL_LOOP = 'LOOP'
        self.TOK_LABEL_NUM = 'NUM'

        self.TOK_ADD = 'ADD'

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

def main():
    # Create a TestLoader and discover all tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    print('YAY')

    suite.addTests(loader.loadTestsFromTestCase(UT_parse_add.TestParseAdd))

    # Run the tests using TextTestRunner
    runner = unittest.TextTestRunner()
    result = runner.run(suite)