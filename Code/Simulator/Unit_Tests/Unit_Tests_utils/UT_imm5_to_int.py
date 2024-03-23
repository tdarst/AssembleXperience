import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestImm5ToInt(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test hash_to_int('#5') == 5
    def test_Given_hash5_Produce_CorrectIntValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_int(test_vars.imm5_val_5), 5)

    # Test hash_to_int('#12') == 12
    def test_Given_hash12_Produce_CorrectIntValue(self):
        test_vars = self.test_vars
        self.assertEqual(utils.hash_to_int(test_vars.imm5_val_12), 12)