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
                               UT_hash_to_int,
                               UT_hash_to_bin,
                               UT_imm5_to_bin,
                               UT_imm5_to_int,
                               UT_hex_to_int,
                               UT_hex_to_bin,
                               UT_bin_to_hash,
                               UT_is_register,
                               UT_is_imm5,
                               UT_is_label,
                               UT_is_offset6,
                               UT_calc_twos_complement,
                               UT_calc_offset9,
                               UT_calc_offset11,
                               UT_get_nzp_bin_string)

from .Unit_Tests_validlib import (UT_valid_add,
                                  UT_valid_and,
                                  UT_valid_jmp,
                                  UT_valid_jsrr,
                                  UT_valid_ld,
                                  UT_valid_ldi,
                                  UT_valid_lea,
                                  UT_valid_ldr,
                                  UT_valid_str,
                                  UT_valid_st,
                                  UT_valid_sti,
                                  UT_valid_ret,
                                  UT_valid_rti,
                                  UT_valid_end,
                                  UT_valid_br,
                                  UT_valid_jsr,
                                  UT_valid_not,
                                  UT_valid_trap,
                                  UT_valid_explicit_trap,
                                  UT_valid_orig,
                                  UT_valid_fill,
                                  UT_valid_blkw)

from .Unit_Tests_disaslib import (UT_disas_add)

# ==============================================================================
# Name: parselib_Tests
# Purpose: Loads all of the parselib unit tests into a test suite and returns it
# ==============================================================================
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

# ==============================================================================
# Name: utils_Tests
# Purpose: Loads all of the utils unit tests into a test suite and returns it
# ==============================================================================
def utils_Tests():
    # Create a TestLoader and Suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all of the tests into the suite
    suite.addTests(loader.loadTestsFromTestCase(UT_int_to_bin.TestIntToBin))

    suite.addTests(loader.loadTestsFromTestCase(UT_hash_to_int.TestHashToInt))
    suite.addTests(loader.loadTestsFromTestCase(UT_hash_to_bin.TestHashToBin))
    suite.addTests(loader.loadTestsFromTestCase(UT_hex_to_int.TestHexToInt))
    suite.addTests(loader.loadTestsFromTestCase(UT_hex_to_bin.TestHexToBin))
    suite.addTests(loader.loadTestsFromTestCase(UT_bin_to_hash.TestBinToHash))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_register.TestIsRegister))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_imm5.TestIsImm5))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_label.TestIsLabel))
    suite.addTests(loader.loadTestsFromTestCase(UT_is_offset6.TestIsOffset6))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_twos_complement.TestCalcTwosComplement))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_offset9.TestCalcOffset9))
    suite.addTests(loader.loadTestsFromTestCase(UT_calc_offset11.TestCalcOffset11))
    suite.addTests(loader.loadTestsFromTestCase(UT_get_nzp_bin_string.TestGetNzpBinString))
    suite.addTests(loader.loadTestsFromTestCase(UT_imm5_to_int.TestImm5ToInt))
    suite.addTests(loader.loadTestsFromTestCase(UT_imm5_to_bin.TestImm5ToBin))

    return suite

def validlib_Tests():
    # Create a TestLoader and Suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all of the tests into the suite
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_add.TestValidAdd))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_and.TestValidAnd))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_jmp.TestValidJmp))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_jsrr.TestValidJsrr))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_ld.TestValidLd)) 
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_ldi.TestValidLdi)) 
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_lea.TestValidLea)) 
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_ldr.TestValidLdr))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_str.TestValidStr))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_st.TestValidSt))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_sti.TestValidSti))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_ret.TestValidRet))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_rti.TestValidRti))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_end.TestValidEnd))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_br.TestValidBr))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_jsr.TestValidJsr))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_not.TestValidNot))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_trap.TestValidTrap))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_explicit_trap.TestValidExplicitTrap))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_orig.TestValidOrig))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_fill.TestValidFill))
    suite.addTests(loader.loadTestsFromTestCase(UT_valid_blkw.TestValidBlkw))
    
    return suite

def disaslib_Tests():
    # Create a TestLoader and Suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(UT_disas_add.TestDisasAdd))

# ==============================================================================
# Name: main
# Purpose: When called, loads all of the unit tests and then runs them.
# ==============================================================================
def main():
    # Generate the test suites
    suite_parselib = parselib_Tests()
    suite_utils = utils_Tests()
    suite_validlib = validlib_Tests()
    suite_disaslib = disaslib_Tests()

    # Run the tests using TextTestRunner
    runner = unittest.TextTestRunner()
    print("\n --- Running parselib unit tests ---")
    runner.run(suite_parselib)
    print("\n --- Running utils unit tests ---")
    runner.run(suite_utils)
    print("\n --- Running validlib unit tests ---")
    runner.run(suite_validlib)
    print("\n --- Running disaslib unit tests ---")
    runner.run(suite_disaslib)