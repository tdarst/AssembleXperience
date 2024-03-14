import re

# Keep in mind the upper limit of range in python is not included
IMM5_INT_RANGE = range(-16, 16)
OFFSET6_INT_RANGE = range(-32, 32)
IMM16_INT_RANGE = range(-32768, 32768)
BLKW_INT_RANGE = range(1, 501)
STRINGZ_INT_RANGE = range(0, 501)

# String values for opcodes that only have one possible translation
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
    'R7':0x7,
    
    
    'r0':0x0,
    'r1':0x1,
    'r2':0x2,
    'r3':0x3,
    'r4':0x4,
    'r5':0x5,
    'r6':0x6,
    'r7':0x7
}

# Length: 8 bits
# Dictionary of all traps and their vectors.
TRAPS = {
    'GETC'  : 0x20,
    'OUT'   : 0x21,
    'PUTS'  : 0x22,
    'IN'    : 0x23,
    'PUTSP' : 0x24,
    'HALT'  : 0x25,
    
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

    'BR'   : 0x0,
    'BRN'  : 0x0,
    'BRZ'  : 0x0,
    'BRP'  : 0x0,
    'BRNZ' : 0x0,
    'BRNP' : 0x0,
    'BRZP' : 0x0,
    'BRNZP': 0x0,

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

def in_range(num: int, val_range: range) -> bool:
    try:
        return num in val_range
    except:
        return False
    
def convert_to_python_hex_format(hex_str: str) -> str:
    index_found = hex_str.find('x')
    converted_str = hex_str[:index_found] + '0' + hex_str[index_found:]
    return converted_str

# ==============================================================================
# Name: int_to_bin
# Purpose: returns the POSITIVE binary string for a given int
# ==============================================================================
def int_to_bin(num: int) -> str:
    return bin(num)[2:] if num >= 0 else bin(num)[3:]

# ==============================================================================
# Name: hash_to_int
# Purpose: returns the int value for a given imm5.
# ==============================================================================
def hash_to_int(imm_str: str) -> int:
    return int(imm_str.replace('#', ''))

# ==============================================================================
# Name: hash_to_bin
# Purpose: returns the binary value for a given imm5.
# ==============================================================================
def hash_to_bin(imm_str: str) -> str:
    return int_to_bin(hash_to_int(imm_str))

# ==============================================================================
# Name: hex_to_int
# Purpose: returns the int value for a given hex.
# ==============================================================================
def hex_to_int(hex_str: str) -> int:
    if not '0x' in hex_str:
        hex_str = convert_to_python_hex_format(hex_str)
    return int(hex_str, 16)

# ==============================================================================
# Name: hex_to_bin
# Purpose: returns the bin value for a given hex
# ==============================================================================
def hex_to_bin(hex_str: str) -> str:
    return int_to_bin(hex_to_int(hex_str))

# ==============================================================================
# Name: bin_to_int
# Purpose: returns the int value for a given bin
# ==============================================================================
def bin_to_int(bin_str: str) -> str:
    return int(bin_str, 2)

# ==============================================================================
# Name: is_register
# Purpose: returns True if token is a valid register, False otherwise.
# ==============================================================================
def is_register(tok: str) -> bool:
    return tok in REGISTERS

# ==============================================================================
# Name: is_bin
# Purpose: returns True if token is a valid binary string, False otherwise.
# ==============================================================================
def is_bin(tok: str) -> bool:
    hex_pattern = re.compile(r'^[01]+$')
    return bool(hex_pattern.match(tok))

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
# Name: is_hash
# Purpose: returns True if token is a valid hash number value, False otherwise.
#          example: #5 or #1000 should return true, #asdaf or 10 should not.
# ==============================================================================
def is_hash(tok: str) -> bool:
    hash_pattern = re.compile(r'^#-?[0-9]*$')
    return bool(hash_pattern.match(tok))

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
# Name: is_hex
# Purpose: returns True if token is a valid hex value, False
#
# Supports prefixes: x, 0x, -x, -0x
# Examples: x3000, 0x3000, -x3000, -0x3000
# ==============================================================================
def is_hex(tok: str) -> bool:
    hex_pattern = re.compile(r'^-?0?x[0-9a-fA-F]+$')
    return bool(hex_pattern.match(tok))

# ==============================================================================
# Name: is_imm16
# Purpose: returns True if token has a valid integer value in the range of
#          signed 16 bit integers.
# ==============================================================================
def is_imm16(tok: str) -> bool:
    val = None
    tok_is_imm16 = False

    if is_hex(tok):
        val = hex_to_int(tok)

    elif is_bin(tok):
        val = bin_to_int(tok)

    elif is_hash(tok):
        val = hash_to_int(tok)

    if val and val in IMM16_INT_RANGE:
        tok_is_imm16 = True

    return tok_is_imm16

def is_blkw_valid_val(tok: str) -> bool:
    val = None
    tok_is_valid = False

    if is_hex(tok):
        val = hex_to_int(tok)

    elif is_bin(tok):
        val = bin_to_int(tok)

    elif is_hash(tok):
        val = hash_to_int(tok)

    if val and val in BLKW_INT_RANGE:
        tok_is_valid = True

    return tok_is_valid

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

# ===============================================================================
# Name: lookup_all_caps
# Purpose: Safe dictionary lookup guaranteeing uppercase match.
# ===============================================================================
def lookup_all_caps(key_to_lookup, dictionary):
    try:
        return dictionary[key_to_lookup.upper()]
    except:
        return None
    
def write_to_file(content_to_write, file_path):
    try:
        with open(file_path, 'w') as new_file:
            new_file.write(content_to_write)
        return True
    except:
        return False
    
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as new_file:
            content = new_file.read()
        return content
    except:
        return None