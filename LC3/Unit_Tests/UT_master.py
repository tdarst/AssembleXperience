# Holds all of the test suites for unit tests.

import unittest
from .Unit_Tests_parseLib import (UT_parse_add,
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

def main():
    # Create a TestLoader and discover all tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #Load all of the tests into the test suite
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

    # Run the tests using TextTestRunner
    runner = unittest.TextTestRunner()
    result = runner.run(suite)