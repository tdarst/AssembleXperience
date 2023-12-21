import os
from collections import namedtuple

# ====================
# Vector Dictionaries
# =====================
REGISTERS = {
    'R0':0x0,
    'R1':0x1,
    'R2':0x2,
    'R3':0x3,
    'R4':0x4,
    'R5':0x5,
    'R6':0x6,
    'R7':0x7
}

TRAPS = {
    'GETC': 0x20,
    'OUT' : 0x21,
    'PUTS': 0x22,
    'IN'  : 0x23,
    'HALT': 0x25
} #PUTS, GETC, etc. 

OPCODE = {
    'BR'   : 0x0,
    'BRn'  : 0x0,
    'BRz'  : 0x0,
    'BRp'  : 0x0,
    'BRnz' : 0x0,
    'BRnp' : 0x0,
    'BRzp' : 0x0,
    'BRnzp': 0x0,

    'ADD' : 0x1,
    'LD'  : 0x2,
    'ST'  : 0x3,
    'JSR' : 0x4,
    'JSRR': 0x4,
    'AND' : 0x5,
    'LDR' : 0x6,
    'STR' : 0X7,
    'RTI' : 0X8,
    'NOT' : 0x9,
    'LDI' : 0xA,
    'STI' : 0xB,
    'JMP' : 0xC,
    'RET' : 0xC,
    'RES' : 0xD,
    'LEA' : 0xE,
    'TRAP': 0xF,

    **TRAPS # includes the TRAPS dictionary
}

PSEUDOS = {
    '.ORIG'   : None,
    '.END'    : None,
    '.FILL'   : None,
    '.BLKW'   : None,
    '.STRINGZ': None
} #.ORIG, .END, etc.

def checkIfValidSymbol(token):
    if '#' in token or '0x' in token:
        return False
    return True

def convertToHex(token):
    if not token.startswith('0'):
        return '0'+token
    return token

def pass1(code_to_parse):

    address_counter = 0x0
    symbol_table = {} # Will be a dictionary of namedtuples

    overall_dictionary = {
        **REGISTERS,
        **OPCODE,
        **PSEUDOS
    }

    # Get rid of any lines that are only comments or are blank
    strippedCode =[x for x in code_to_parse.splitlines() if x and not x.startswith(';')]
    for line in code_to_parse.replace("\t", " ").split("\n"):
        line = line.split(";")[0].strip()

        if not line:
            continue

        label = line.rstrip(":")
        symbol_table[label] = address_counter if ':' in line else address_counter + 1

    return symbol_table

def pass2():
    pass

def main():
    f = open(r'Test_Code\2048.asm', 'r')
    readLines = f.read()
    print(pass1(readLines))

main()