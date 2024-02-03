import unittest
from . import Class_TestVars_utils
import utils

class TestIsLabel(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test is_register('LOOP') == True if LOOP is in label_lookup
    def test_Given_LOOPinLookupTable_Produce_True(self):
        test_vars = self.test_vars
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_LOOP,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertEqual(utils.is_label(test_vars.TOK_LABEL_LOOP, label_lookup), True)

    # Test is_register('LOOP') == True if LOOP is not in label_lookup
    def test_Given_LOOPnotInLookupTable_Produce_False(self):
        test_vars = self.test_vars
        label_lookup = test_vars.generate_tester_label_lookup(label=test_vars.TOK_LABEL_NUM,
                                                              address=test_vars.ADDRESS_0X3001)
        
        self.assertEqual(utils.is_label(test_vars.TOK_LABEL_LOOP, label_lookup), False)

    # Test is_register('LOOP') == True if LOOP is not in label_lookup
    def test_Given_EmptyLabelLookup_Produce_False(self):
        test_vars = self.test_vars
        label_lookup = []
        
        self.assertEqual(utils.is_label(test_vars.TOK_LABEL_LOOP, label_lookup), False)