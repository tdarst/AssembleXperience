import unittest
from . import Class_TestVars_utils
from ...Supporting_Libraries import utils

class TestGetNzpAsmString(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test get_nzp_bin_string('BRn') == '100'
    def test_Given_100_Produce_BRn(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_100), 'n')

    # Test get_nzp_bin_string('BRnz') == '110'
    def test_Given_110_Produce_BRnz(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_110), 'nz')

    # Test get_nzp_bin_string('BRnzp') == '111'
    def test_Given_111_Produce_BRnzp(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_111), 'nzp')

    # Test get_nzp_bin_string('BRz') == '010'
    def test_Given_010_Produce_BRz(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_010), 'z')

    # Test get_nzp_bin_string('BRzp') == '011'
    def test_Given_011_Produce_BRzp(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_011), 'zp')

    # Test get_nzp_bin_string('BRp') == '001'
    def test_Given_001_Produce_BRp(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_asm_string(test_vars.nzp_001), 'p')