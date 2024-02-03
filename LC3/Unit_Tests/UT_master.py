# Holds all of the test suites for unit tests.

import unittest
from .Unit_Tests_parselib import (UT_parse_add,
                                  UT_parse_and,
                                  UT_parse_br,
                                  UT_parse_jmp,
                                  UT_parse_jsr,
                                  UT_parse_jsrr,
                                  UT_parse_ld,
                                  UT_parse_ldi,
                                  UT_parse_ldr,
                                  UT_parse_lea,
                                  UT_parse_not,
                                  UT_parse_ret,
                                  UT_parse_rti,
                                  UT_parse_st,
                                  UT_parse_sti,
                                  UT_parse_str,
                                  UT_parse_trap,
                                  UT_parse_explicit_trap,
                                  UT_parse_orig,
                                  UT_parse_fill,
                                  UT_parse_blkw,
                                  UT_parse_stringz)

from .Unit_Tests_utils import (UT_int_to_bin,
                               UT_imm5_to_int,
                               UT_imm5_to_bin,
                               UT_hex_to_int,
                               UT_hex_to_bin,
                               UT_is_register,
                               UT_is_imm5,
                               UT_is_label,
                               UT_is_offset6,
                               UT_calc_twos_complement,
                               UT_calc_offset9,
                               UT_calc_offset11,
                               UT_get_nzp_bin_string)

def parselib_Tests():
    # Create a TestLoader and Suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all of the tests into the suite
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_add.TestParseAdd))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_and.TestParseAnd))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_br.TestParseBr))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_jmp.TestParseJmp))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_jsr.TestParseJsr))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_jsrr.TestParseJsrr))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_ld.TestParseLd))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_ldi.TestParseLdi))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_ldr.TestParseLdr))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_lea.TestParseLea))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_not.TestParseNot))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_ret.TestParseRet))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_rti.TestParseRti))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_st.TestParseSt))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_sti.TestParseSti))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_str.TestParseStr))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_trap.TestParseTrap))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_explicit_trap.TestParseExplicitTrap))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_orig.TestParseOrig))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_fill.TestParseFill))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_blkw.TestParseBlkw))
    suite.addTests(loader.loadTestsFromTestCase(UT_parse_stringz.TestParseStringz))

    return suite

def utils_Tests():
    # Create a TestLoader and Suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all of the tests into the suite
    suite.addTests(loader.loadTestsFromTestCase(UT_int_to_bin.TestIntToBin))
    suite.addTests(loader.loadTestsFromTestCase(UT_imm5_to_int.TestImm5ToInt))
    suite.addTests(loader.loadTestsFromTestCase(UT_imm5_to_bin.TestImm5ToBin))
    suite.addTests(loader.loadTestsFromTestCase(UT_hex_to_int.TestHexToInt))
    suite.addTests(loader.loadTestsFromTestCase(UT_hex_to_bin.TestHexToBin))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_register.TestIsRegister))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_imm5.TestIsImm5))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_label.TestIsLabel))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_offset6.TestIsOffset6))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_twos_complement.TestCalcTwosComplement))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_offset9.TestCalcOffset9))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_offset11.TestCalcOffset11))
    suite.addTests(loader.loadTestsFromTestCase(UT_get_nzp_bin_string.TestGetNzpBinString))

    return suite

def main():
    # Generate the test suites
    suite_parse_lib = parselib_Tests()
    suite_utils = utils_Tests()

    # Run the tests using TextTestRunner
    runner = unittest.TextTestRunner()
    print("\n --- Running parselib unit tests ---")
    runner.run(suite_parse_lib)
    print("\n --- Running utils unit tests ---")
    runner.run(suite_utils)