IMM5_INT_RANGE = range(-16, 16)
OFFSET6_INT_RANGE = range(-32, 32)

RET_BIN_STRING = '1100000111000000'
RTI_BIN_STRING = '1000000000000000'

ORIG_OPCODE_NAME = '.ORIG'

# 3 bits
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

# 8 bits
TRAPS = {
    'GETC'  : 0x20,
    'OUT'   : 0x21,
    'PUTS'  : 0x22,
    'IN'    : 0x23,
    'PUTSP' : 0x24,
    'HALT'  : 0x25
} #PUTS, GETC, etc. 

# 4 bits
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
}

overall_dictionary = {
    **OPCODE,
    **REGISTERS,
    **PSEUDOS
}

opcode_dictionary = {
    **OPCODE,
    **PSEUDOS
}

KEY_OPCODE = 'opcode'
KEY_OPERANDS = 'operands'
KEY_LABELS = 'labels'

def int_to_bin(num: int) -> str:
    return bin(num)[2:] if num >= 0 else bin(num)[3:]

def imm5_to_int(imm_str: str) -> int:
    return int(imm_str.replace('#', ''))

def imm5_to_bin(imm_str: str) -> str:
    return int_to_bin(imm5_to_int(imm_str))

def hex_to_int(hex_str: str) -> int:
    return int(hex_str, 16)

def hex_to_bin(hex_str: str) -> str:
    return int_to_bin(hex_to_int(hex_str))

def is_register(tok: str) -> bool:
    return tok in REGISTERS

#TODO: FIX THIS RETURN
def is_imm5(tok: str) -> bool:
    try:
        isImm5 = tok.startswith('#') \
                 and int(tok.replace('#','')) in IMM5_INT_RANGE # This specifies min -16, max 15
    except:
        isImm5 = False

    return isImm5
    
def is_label(tok: str, label_lookup: dict) -> bool:
    tok_is_label = tok in label_lookup
    return tok_is_label

def is_offset6(tok: str) -> bool:
    try:
        isOffset6 = tok.startswith('#') \
        and int(tok.replace('#','')) in OFFSET6_INT_RANGE
    except:
        isOffset6 = False
    
    return isOffset6

# Takes positive binary string and returns it's two's complement
def calc_twos_complement(bin_string: str):
    if not all(bit == '0' for bit in bin_string):
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in bin_string)
        twos_complement = int_to_bin(int(inverted_bits, 2) + 1)
    else:
        twos_complement = '0000'
        
    return twos_complement

def calc_offset9(label_address: str, current_address: str) -> str:
    label_address = hex_to_int(label_address)
    current_address = hex_to_int(current_address)
    int_offset = label_address - current_address - 1
    if int_offset < 0:
        offset9 = calc_twos_complement(int_to_bin(int_offset).zfill(9))
    else:
        offset9 = int_to_bin(int_offset).zfill(9)

    return offset9

def calc_offset11(label_address: str, current_address: str) -> str:
    label_address = hex_to_int(label_address)
    current_address = hex_to_int(current_address)
    int_offset = label_address - current_address - 1
    if int_offset < 0:
        offset11 = calc_twos_complement(int_to_bin(int_offset).zfill(11))
    else:
        offset11 = int_to_bin(int_offset).zfill(11)

    return offset11

def get_nzp_bin_string(opcode: str) -> str:
    nzp = [int('n' in opcode), int('z' in opcode), int('p' in opcode)]

    nzp_string = ''.join([str(item) for item in nzp]) \
                 if sum(nzp) > 0 \
                 else '111'
    
    return nzp_string