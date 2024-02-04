from . import utils

def validate_line(): pass

# ===============================================================================
# Name: validate_add_and
# Purpose: Determines whether line is a valid use of ADD or AND.
# ===============================================================================
def validate_add_and(tokens: dict, label_lookup: dict):
    pass

def validate_jmp_jsrr(): pass

def validate_ld_ldi_lea(): pass

def validate_ldr_str(): pass

def validate_st_sti(): pass

def validate_br(): pass

def validate_jsr(): pass

def validate_not(): pass

def validate_trap(): pass

def validate_explicit_trap(): pass

def validate_orig(): pass

def validate_fill(): pass

def validate_blkw(): pass

def validate_stringz(): pass

def validate_add(tokens: dict, label_lookup: dict):
    return validate_add_and(tokens, label_lookup)

def validate_and(tokens: dict, label_lookup: dict):
    return validate_add_and(tokens, label_lookup)

def validate_jmp(): pass

def validate_ld(): pass

def validate_ldi(): pass

def validate_ldr(): pass

def validate_lea(): pass

def validate_ret(): pass

def validate_rti(): pass

def validate_st(): pass

def validate_sti(): pass

def validate_end(): pass
    
# PARSE_DICT is used to map all opcode tokens to their respective parsing functions
PARSE_DICT = {
    'BR'   : None,
    'BRn'  : None,
    'BRz'  : None,
    'BRp'  : None,
    'BRnz' : None,
    'BRnp' : None,
    'BRzp' : None,
    'BRnzp': None,

    'ADD' : validate_add,
    'LD'  : None,
    'ST'  : None,
    'JSR' : None,
    'JSRR': None,
    'AND' : validate_and,
    'LDR' : None,
    'STR' : None,
    'RTI' : None,
    'NOT' : None,
    'LDI' : None,
    'STI' : None,
    'JMP' : None,
    'RET' : None,
    'LEA' : None,

    'TRAP': None,
    'GETC': None,
    'OUT' : None,
    'PUTS': None,
    'IN'  : None,
    'HALT': None,

    '.ORIG': None,
    '.END' : None,
    '.FILL': None,
    '.BLKW': None,
    '.STRINGZ': None
}    