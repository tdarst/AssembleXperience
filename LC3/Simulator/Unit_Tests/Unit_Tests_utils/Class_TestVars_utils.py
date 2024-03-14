from ..Unit_Tests_parselib import Class_TestVars_parselib

# =============================================================================
# Name: TestVars_utils
# Purpose: Creates variables to be used for testing so that I can reuse them
#          easily and also leaves less floating strings in the unit tests.
#          inherits TestVars which is the class used in parselib unit tests
#          mainly for it's generate symbol table and label lookup functions.
# =============================================================================
class TestVars_utils(Class_TestVars_parselib.TestVars):
    def __init__(self):
        super().__init__()
        self.int_val_1 = 1
        self.int_val_2 = 2
        self.int_val_3 = 3
        self.int_val_10 = 10
        self.int_val_100 = 100

        self.imm5_val_5 = '#5'
        self.imm5_val_12 = '#12'
        self.imm5_val_neg16 = '#-16'
        self.imm5_val_15 = '#15'
        self.fake_imm5_neg17 = '#-17'
        self.fake_imm5_16 = '#16'

        self.offset6_val_5 = '#5'
        self.offset6_val_neg32 = '#-32'
        self.offset6_val_31 = '#31'
        self.fake_offset6_val_neg33 = '#-33'
        self.fake_offset6_val_32 = "#32"


        self.hex_val_0x3000 = '0x3000'
        self.hex_val_x3000 = 'x3000'
        self.hex_val_0x005 = '0x005'
        self.address_0x3000 = '0x3000'
        self.address_0x3010 = '0x3010'

        self.reg_R0 = 'R0'
        self.reg_R1 = 'R1'
        self.reg_R2 = 'R2'
        self.reg_R3 = 'R3'
        self.reg_R4 = 'R4'
        self.reg_R5 = 'R5'
        self.reg_R6 = 'R6'
        self.reg_R7 = 'R7'
        self.reg_R8 = 'R8'

        self.bin_1101 = '1101'
        self.bin_0011 = '0011'
        self.bin_0000 = '0000'
        self.bin_1 = '1'


        self.nonsense = 'alkajsdflkj'