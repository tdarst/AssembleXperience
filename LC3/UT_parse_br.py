import unittest
import Class_TestVars
import parselib

class TestParseBr(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars.TestVars()

    # Test
    # x3000 BRp LOOP
    # x3001 LOOP
    def test_Given_BR_LABEL_Offset_Positive_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BR, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000111000000000')

    # Test
    # x3000 LOOP
    # x3001 BRp LOOP
    def test_Given_BR_LABEL_Offset_Negative_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3001
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BR, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3000)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0101001001100001')

    # Test
    # x3000 BRn LOOP
    # x3001 LOOP
    def test_Given_BRN_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRN, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000100000000000')

    # Test
    # x3000 BRnp LOOP
    # x3001 LOOP
    def test_Given_BRNP_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRNP, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000101000000000')

    # Test
    # x3000 BRnz LOOP
    # x3001 LOOP
    def test_Given_BRNZ_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRNZ, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000110000000000')

    # Test
    # x3000 BRnzp LOOP
    # x3001 LOOP
    def test_Given_BRNZP_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRNZP, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000111000000000')

    # Test
    # x3000 BRz LOOP
    # x3001 LOOP
    def test_Given_BRZ_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRZ, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000010000000000')

    # Test
    # x3000 BRzp LOOP
    # x3001 LOOP
    def test_Given_BRZP_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRZP, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000011000000000')

    # Test
    # x3000 BRp LOOP
    # x3001 LOOP
    def test_Given_BRP_LABEL_Produce_Correct_BinString(self):
        test_vars = self.test_vars
        address = test_vars.ADDRESS_0X3000
        tokens = test_vars.generate_tester_symbol_table(opcode=test_vars.TOK_BRP, 
                                                        operands=[test_vars.TOK_LABEL_LOOP], 
                                                        labels=[test_vars.TOK_LABEL_LOOP])
        
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertTrue(parselib.parse_br(address, tokens, label_lookup), '0000001000000000')