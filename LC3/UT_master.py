import unittest
import UT_parse_add
import UT_parse_and
import UT_parse_br
import UT_parse_jmp
import UT_parse_jsr
import UT_parse_jsrr
import UT_parse_ld
import UT_parse_ldi
import UT_parse_ldr
import UT_parse_lea
import UT_parse_not
import UT_parse_ret
import UT_parse_rti
import UT_parse_st
import UT_parse_sti
import UT_parse_str
import UT_parse_trap
import UT_parse_explicit_trap
import UT_parse_orig
import UT_parse_fill
import UT_parse_blkw
import UT_parse_stringz

def main():
    # Create a TestLoader and discover all tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

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