IMM5_INT_RANGE = range(-16, 16)
OFFSET6_INT_RANGE = range(-32, 32)

RET_BIN_STRING = '1100000111000000'
RTI_BIN_STRING = '1000000000000000'

ORIG_OPCODE_NAME = '.ORIG'

# Length: 3 bits
# Dictioanry of all registers and their vectors.
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

# Length: 8 bits
# Dictionary of all traps and their vectors.
TRAPS = {
    'GETC'  : 0x20,
    'OUT'   : 0x21,
    'PUTS'  : 0x22,
    'IN'    : 0x23,
    'PUTSP' : 0x24,
    'HALT'  : 0x25
} #PUTS, GETC, etc. 

# Length: 4 bits
# Dictionary of all opcodes and their vectors.
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

# Dictionary of all pseudo-ops and their (non-existant) vectors.
PSEUDOS = {
    '.ORIG'   : None,
    '.END'    : None,
    '.FILL'   : None,
    '.BLKW'   : None,
    '.STRINGZ': None
}

# Dictionary of all valid operations
overall_dictionary = {
    **OPCODE,
    **REGISTERS,
    **PSEUDOS
}

# Dictionary of all opcodes
opcode_dictionary = {
    **OPCODE,
    **PSEUDOS
}

# Strings for symbol_table keys
KEY_OPCODE = 'opcode'
KEY_OPERANDS = 'operands'
KEY_LABELS = 'labels'

# ==============================================================================
# Name: int_to_bin
# Purpose: returns the POSITIVE binary string for a given int
# ==============================================================================
def int_to_bin(num: int) -> str:
    return bin(num)[2:] if num >= 0 else bin(num)[3:]

# ==============================================================================
# Name: imm5_to_int
# Purpose: returns the int value for a given imm5.
# ==============================================================================
def imm5_to_int(imm_str: str) -> int:
    return int(imm_str.replace('#', ''))

# ==============================================================================
# Name: imm5_to_int
# Purpose: returns the binary value for a given imm5.
# ==============================================================================
def imm5_to_bin(imm_str: str) -> str:
    return int_to_bin(imm5_to_int(imm_str))

# ==============================================================================
# Name: imm5_to_int
# Purpose: returns the int value for a given hex.
# ==============================================================================
def hex_to_int(hex_str: str) -> int:
    return int(hex_str, 16)

# ==============================================================================
# Name: hex_to_bin
# Purpose: returns the hex value for a given bin
# ==============================================================================
def hex_to_bin(hex_str: str) -> str:
    return int_to_bin(hex_to_int(hex_str))

# ==============================================================================
# Name: is_register
# Purpose: returns True if token is a valid register, False otherwise.
# ==============================================================================
def is_register(tok: str) -> bool:
    return tok in REGISTERS

# ==============================================================================
# Name: is_imm5
# Purpose: returns True if token is a valid imm5 value, False otherwise.
# ==============================================================================
def is_imm5(tok: str) -> bool:
    try:
        isImm5 = tok.startswith('#') \
                 and int(tok.replace('#','')) in IMM5_INT_RANGE # This specifies min -16, max 15
    except:
        isImm5 = False

    return isImm5

# ==============================================================================
# Name: is_label
# Purpose: returns True if token is a valid label, False otherwise. Bases this
#          on whether it exists in the label_lookup.
# ==============================================================================
def is_label(tok: str, label_lookup: dict) -> bool:
    tok_is_label = tok in label_lookup
    return tok_is_label

# ==============================================================================
# Name: is_offset6
# Purpose: returns True if token is a valid offset6 value, False otherwise.
# ==============================================================================
def is_offset6(tok: str) -> bool:
    try:
        isOffset6 = tok.startswith('#') \
        and int(tok.replace('#','')) in OFFSET6_INT_RANGE
    except:
        isOffset6 = False
    
    return isOffset6

# ==============================================================================
# Name: calc_twos_complement
# Purpose: returns the twos complement of any given binary string.
# ==============================================================================
def calc_twos_complement(bin_string: str):
    if not all(bit == '0' for bit in bin_string):
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in bin_string)
        twos_complement = int_to_bin(int(inverted_bits, 2) + 1)
    else:
        twos_complement = '0000'
        
    return twos_complement

# ==============================================================================
# Name: calc_offset9
# Purpose: Calculates 9 bit offset value from given current and label addresses.
# ==============================================================================
def calc_offset9(label_address: str, current_address: str) -> str:
    label_address = hex_to_int(label_address)
    current_address = hex_to_int(current_address)
    int_offset = label_address - current_address - 1
    if int_offset < 0:
        offset9 = calc_twos_complement(int_to_bin(int_offset).zfill(9))
    else:
        offset9 = int_to_bin(int_offset).zfill(9)

    return offset9

# ===============================================================================
# Name: calc_offset11
# Purpose: Calculates 11 bit offset value from given current and label addresses.
# ===============================================================================
def calc_offset11(label_address: str, current_address: str) -> str:
    label_address = hex_to_int(label_address)
    current_address = hex_to_int(current_address)
    int_offset = label_address - current_address - 1
    if int_offset < 0:
        offset11 = calc_twos_complement(int_to_bin(int_offset).zfill(11))
    else:
        offset11 = int_to_bin(int_offset).zfill(11)

    return offset11

# ===============================================================================
# Name: get_nzp_bin_string
# Purpose: Given a BR opcode, returns it's nzp string. If opcode is just 'BR'
#          (as opposed to say BRn), returns '111'
# ===============================================================================
def get_nzp_bin_string(opcode: str) -> str:
    nzp = [int('n' in opcode), int('z' in opcode), int('p' in opcode)]

    nzp_string = ''.join([str(item) for item in nzp]) \
                 if sum(nzp) > 0 \
                 else '111'
    
    return nzp_string