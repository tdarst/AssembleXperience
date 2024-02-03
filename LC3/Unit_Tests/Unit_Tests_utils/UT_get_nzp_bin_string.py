import unittest
from . import Class_TestVars_utils
import utils

class TestGetNzpBinString(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        self.test_vars = Class_TestVars_utils.TestVars_utils()

    # Test get_nzp_bin_string('BR') == '111'
    def test_Given_BR_Produce_111(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BR), '111')

    # Test get_nzp_bin_string('BRn') == '100'
    def test_Given_BRn_Produce_100(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRN), '100')

    # Test get_nzp_bin_string('BRnz') == '110'
    def test_Given_BRnz_Produce_110(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRNZ), '110')

    # Test get_nzp_bin_string('BRnz') == '111'
    def test_Given_BRnzp_Produce_111(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRNZP), '111')

    # Test get_nzp_bin_string('BRz') == '010'
    def test_Given_BRz_Produce_010(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRZ), '010')

    # Test get_nzp_bin_string('BRzp') == '011'
    def test_Given_BRzp_Produce_011(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRZP), '011')

    # Test get_nzp_bin_string('BRp') == '001'
    def test_Given_BRP_Produce_001(self):
        test_vars = self.test_vars
        self.assertEqual(utils.get_nzp_bin_string(test_vars.TOK_BRP), '001')