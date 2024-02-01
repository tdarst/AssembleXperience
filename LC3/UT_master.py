import unittest
import UT_parse_add

def main():
    # Create a TestLoader and discover all tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(UT_parse_add.TestParseAdd))

    # Run the tests using TextTestRunner
    runner = unittest.TextTestRunner()
    result = runner.run(suite)