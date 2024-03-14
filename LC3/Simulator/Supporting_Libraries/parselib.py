# Library of functions to parse different lines.
from . import utils

MAX_LINE_LENGTH = 16
OPCODE_LENGTH = 4
REGISTER_LENGTH = 3

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

# =============================================================================
# Name: parse_add_or_and
# Purpose: Takes tokens for ADD and AND operations and turns them into their
#          binary equivalent
# =============================================================================
def parse_add_or_and(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    OP1, OP2, OP3 = operands[0], operands[1], operands[2]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_OP1 = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    bin_OP2 = utils.int_to_bin(utils.REGISTERS[OP2]).zfill(REGISTER_LENGTH)

    if utils.is_register(OP3):
        bin_OP3 = utils.int_to_bin(utils.REGISTERS[OP3]).zfill(6)

    elif utils.is_imm5(OP3):
        bin_OP3 = '1'
        bin_OP3 += utils.hash_to_bin(OP3).zfill(5)

    bin_string = bin_opcode + bin_OP1 + bin_OP2 + bin_OP3

    return bin_string

# =============================================================================
# Name: parse_jmp_or_jsrr
# Purpose: Takes tokens for JMP and JSRR operations and turns them into their
#          binary equivalent
# =============================================================================
def parse_jmp_or_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    OP1 = tokens[KEY_OPERANDS][0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    fill_zeros3 = ''.zfill(3)
    bin_reg = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    fill_zeros6 = ''.zfill(6)

    bin_string = bin_opcode + fill_zeros3 + bin_reg + fill_zeros6

    return bin_string

# ================================================================================
# Name: parse_ld_ldi_lea
# Purpose: Takes tokens for LD, LDI, AND LEA operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_ld_ldi_lea(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    dest_reg = operands[0]
    label = operands[1]
    label_address = label_lookup[label]
    current_address = address

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_dest_reg = utils.int_to_bin(utils.REGISTERS[dest_reg]).zfill(REGISTER_LENGTH)
    offset9_string = utils.calc_offset9(label_address, current_address)

    bin_string = bin_opcode + bin_dest_reg + offset9_string

    return bin_string

# ================================================================================
# Name: parse_ldr_str
# Purpose: Takes tokens for LDR operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_ldr_str(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    OP1, OP2, OP3 = operands[0], operands[1], operands[2]
    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_OP1 = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    bin_OP2 = utils.int_to_bin(utils.REGISTERS[OP2]).zfill(REGISTER_LENGTH)

    bin_string = bin_opcode + bin_OP1 + bin_OP2

    if utils.is_imm5(OP3):
        bin_OP3 = utils.hash_to_bin(OP3).zfill(6)
        bin_string += bin_OP3

    else:
        bin_OP3 = utils.hex_to_bin(OP3).zfill(6)
        bin_string += bin_OP3

    return bin_string

# ================================================================================
# Name: parse_br
# Purpose: Takes tokens for BR operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_br(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    label = operands[0]
    current_address = address
    label_address = label_lookup[label]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    nzp_string = utils.get_nzp_bin_string(opcode)
    offset9_string = utils.calc_offset9(label_address, current_address)

    bin_string = bin_opcode + nzp_string + offset9_string
    return bin_string

# ================================================================================
# Name: parse_jsr
# Purpose: Takes tokens for JSR operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_jsr(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    label = tokens[KEY_OPERANDS][0]
    label_address = label_lookup[label]
    current_address = address

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    fill_one = '1'
    offset11_string = utils.calc_offset11(label_address, current_address)

    bin_string = bin_opcode + fill_one + offset11_string

    return bin_string

# ================================================================================
# Name: parse_not
# Purpose: Takes tokens for NOT operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_not(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    dest_reg = operands[0]
    src_reg = operands[1]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_DR = utils.int_to_bin(utils.REGISTERS[dest_reg]).zfill(REGISTER_LENGTH)
    bin_SR = utils.int_to_bin(utils.REGISTERS[src_reg]).zfill(REGISTER_LENGTH)
    end_str = '1'*6

    bin_string = bin_opcode + bin_DR + bin_SR + end_str

    return bin_string

# ================================================================================
# Name: parse_st_sti
# Purpose: Takes tokens for ST AND STI operations and turns them into their
#          binary equivalent
# ================================================================================
def parse_st_sti(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    src_reg = operands[0]
    label = operands[1]
    label_address = label_lookup[label]
    current_address = address

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    src_reg = utils.int_to_bin(utils.REGISTERS[src_reg]).zfill(REGISTER_LENGTH)
    offset9_string = offset9_string = utils.calc_offset9(label_address, current_address)

    bin_string = bin_opcode + src_reg + offset9_string

    return bin_string

# ================================================================================
# Name: parse_trap
# Purpose: Takes tokens for TRAP X20 through X25 operations and turns them into 
#          their binary equivalent
# ===============================================================================
def parse_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    trap_vector = operands[0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.hex_to_bin(trap_vector).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

# ================================================================================
# Name: parse_explicit_trap
# Purpose: Takes tokens for trap calls by name (i.e. HALT, GETC, OUT, etc.) and
#          turns them into their binary equivalent
# ===============================================================================
def parse_explicit_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = 'TRAP'
    trap_vector = tokens[KEY_OPCODE]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.int_to_bin(utils.TRAPS[trap_vector]).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

# ================================================================================
# Name: parse_orig
# Purpose: Takes tokens for .ORIG lines and turns them into their binary
#          equivalent.
# ===============================================================================
def parse_orig(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    hex_val = operands[0]

    bin_string = utils.hex_to_bin(hex_val).zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: parse_fill
# Purpose: Takes tokens for .FILL lines and turns them into their binary
#          equivalent.
# ===============================================================================
def parse_fill(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    num_val = operands[0]

    if utils.is_hex(num_val):
        bin_val = utils.hex_to_bin(num_val)
    
    elif utils.is_imm5(num_val):
        bin_val = utils.hash_to_bin(num_val)

    bin_string = bin_val.zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: parse_blkw
# Purpose: Takes tokens for .BLKW lines and turns them into their binary
#          equivalent.
# ===============================================================================
def parse_blkw(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    imm5_val = utils.hash_to_int(operand)
    bin_string = ''
    for i in range(0, imm5_val-1):
        bin_string += ''.zfill(MAX_LINE_LENGTH) + '\n'
    bin_string += ''.zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: parse_stringz
# Purpose: Takes tokens for .STRINGZ lines and turns them into their binary
#          equivalent.
# ===============================================================================
def parse_stringz(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    bin_string = ''
    for char in operand:
        bin_char = utils.int_to_bin(ord(char)).zfill(MAX_LINE_LENGTH)
        bin_string += bin_char + '\n'
    bin_string += ''.zfill(MAX_LINE_LENGTH)
    
    return bin_string

# ===============================================================================
# Name: parse_add
# Purpose: Takes tokens for ADD lines and turns them into their binary
#          equivalent. Uses parse_add_or_and.
# ===============================================================================
def parse_add(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_add_or_and(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_and
# Purpose: Takes tokens for AND lines and turns them into their binary
#          equivalent. Uses parse_add_or_and.
# ===============================================================================
def parse_and(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_add_or_and(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_jmp
# Purpose: Takes tokens for JMP lines and turns them into their binary
#          equivalent. Uses parse_jmp_or_jsrr.
# ===============================================================================
def parse_jmp(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_jmp_or_jsrr(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_jsrr
# Purpose: Takes tokens for JSRR lines and turns them into their binary
#          equivalent. Uses parse_jmp_or_jsrr.
# ===============================================================================
def parse_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_jmp_or_jsrr(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_ld
# Purpose: Takes tokens for LD lines and turns them into their binary
#          equivalent. Uses parse_ld_ldi_lea.
# ===============================================================================
def parse_ld(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_ldi
# Purpose: Takes tokens for LDI lines and turns them into their binary
#          equivalent. Uses parse_ld_ldi_lea.
# ===============================================================================
def parse_ldi(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_ldr
# Purpose: Takes tokens for LDR lines and turns them into their binary
#          equivalent. Uses parse_ldr_str.
# ===============================================================================
def parse_ldr(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ldr_str(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_lea
# Purpose: Takes tokens for LEA lines and turns them into their binary
#          equivalent. Uses parse_ld_ldi_lea.
# ===============================================================================
def parse_lea(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_ret
# Purpose: RET only ever has one binary translation. Simply returns that
#          binary string.
# ===============================================================================
def parse_ret(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RET_BIN_STRING

# ===============================================================================
# Name: parse_rti
# Purpose: RTI only ever has one binary translation. Simply returns that
#          binary string.
# ===============================================================================
def parse_rti(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RTI_BIN_STRING

# ===============================================================================
# Name: parse_st
# Purpose: Takes tokens for ST lines and turns them into their binary
#          equivalent. Uses parse_st_sti.
# ===============================================================================
def parse_st(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_st_sti(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_sti
# Purpose: Takes tokens for STI lines and turns them into their binary
#          equivalent. Uses parse_st_sti.
# ===============================================================================
def parse_sti(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_st_sti(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_str
# Purpose: Takes tokens for STR lines and turns them into their binary
#          equivalent. Uses parse_ldr_str.
# ===============================================================================
def parse_str(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ldr_str(address, tokens, label_lookup)

# ===============================================================================
# Name: parse_end
# Purpose: END has no binary translation. Simply returns a blank string
# ===============================================================================
def parse_end(address: str, tokens: dict, label_lookup: dict) -> str:
    return ''


# PARSE_DICT is used to map all opcode tokens to their respective parsing functions
PARSE_DICT = {
    'BR'   : parse_br,
    'BRn'  : parse_br,
    'BRz'  : parse_br,
    'BRp'  : parse_br,
    'BRnz' : parse_br,
    'BRnp' : parse_br,
    'BRzp' : parse_br,
    'BRnzp': parse_br,

    'BR'   : parse_br,
    'BRN'  : parse_br,
    'BRZ'  : parse_br,
    'BRP'  : parse_br,
    'BRNZ' : parse_br,
    'BRNP' : parse_br,
    'BRZP' : parse_br,
    'BRNZP': parse_br,

    'ADD' : parse_add,
    'LD'  : parse_ld,
    'ST'  : parse_st,
    'JSR' : parse_jsr,
    'JSRR': parse_jsrr,
    'AND' : parse_and,
    'LDR' : parse_ldr,
    'STR' : parse_str,
    'RTI' : parse_rti,
    'NOT' : parse_not,
    'LDI' : parse_ldi,
    'STI' : parse_sti,
    'JMP' : parse_jmp,
    'RET' : parse_ret,
    'LEA' : parse_lea,

    'TRAP': parse_trap,
    'GETC': parse_explicit_trap,
    'OUT' : parse_explicit_trap,
    'PUTS': parse_explicit_trap,
    'IN'  : parse_explicit_trap,
    'HALT': parse_explicit_trap,

    '.ORIG': parse_orig,
    '.END' : parse_end,
    '.FILL': parse_fill,
    '.BLKW': parse_blkw,
    '.STRINGZ': parse_stringz
}    