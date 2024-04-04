# Library of functions to parse different lines.
from . import utils

MAX_LINE_LENGTH = 16
OPCODE_LENGTH = 4
REGISTER_LENGTH = 3

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

# =============================================================================
# Name: asem_add_or_and
# Purpose: Takes tokens for ADD and AND operations and turns them into their
#          binary equivalent
# =============================================================================
def asem_add_or_and(address: str, tokens: dict, label_lookup: dict) -> str:
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
        bin_OP3 += utils.integer_to_twos_complement(utils.hash_to_int(OP3), 5)

    bin_string = bin_opcode + bin_OP1 + bin_OP2 + bin_OP3

    return bin_string

# =============================================================================
# Name: asem_jmp_or_jsrr
# Purpose: Takes tokens for JMP and JSRR operations and turns them into their
#          binary equivalent
# =============================================================================
def asem_jmp_or_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    OP1 = tokens[KEY_OPERANDS][0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    fill_zeros3 = ''.zfill(3)
    bin_reg = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    fill_zeros6 = ''.zfill(6)

    bin_string = bin_opcode + fill_zeros3 + bin_reg + fill_zeros6

    return bin_string

# ================================================================================
# Name: asem_ld_ldi_lea
# Purpose: Takes tokens for LD, LDI, AND LEA operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_ld_ldi_lea(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_ldr_str
# Purpose: Takes tokens for LDR operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_ldr_str(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_br
# Purpose: Takes tokens for BR operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_br(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_jsr
# Purpose: Takes tokens for JSR operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_jsr(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_not
# Purpose: Takes tokens for NOT operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_not(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_st_sti
# Purpose: Takes tokens for ST AND STI operations and turns them into their
#          binary equivalent
# ================================================================================
def asem_st_sti(address: str, tokens: dict, label_lookup: dict) -> str:
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
# Name: asem_trap
# Purpose: Takes tokens for TRAP X20 through X25 operations and turns them into 
#          their binary equivalent
# ===============================================================================
def asem_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    trap_vector = operands[0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.hex_to_bin(trap_vector).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

# ================================================================================
# Name: asem_explicit_trap
# Purpose: Takes tokens for trap calls by name (i.e. HALT, GETC, OUT, etc.) and
#          turns them into their binary equivalent
# ===============================================================================
def asem_explicit_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = 'TRAP'
    trap_vector = tokens[KEY_OPCODE]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.int_to_bin(utils.TRAPS[trap_vector]).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

# ================================================================================
# Name: asem_orig
# Purpose: Takes tokens for .ORIG lines and turns them into their binary
#          equivalent.
# ===============================================================================
def asem_orig(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    hex_val = operands[0]

    bin_string = utils.hex_to_bin(hex_val).zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: asem_fill
# Purpose: Takes tokens for .FILL lines and turns them into their binary
#          equivalent.
# ===============================================================================
def asem_fill(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    num_val = operands[0]

    if utils.is_hex(num_val):
        bin_val = utils.hex_to_bin(num_val)
    
    elif utils.is_hash(num_val):
        num_val = utils.hash_to_int(num_val)
        if num_val < 0:
            bin_val = utils.one_fill(utils.calc_twos_complement(utils.int_to_bin(num_val)), 16)
        else:
            bin_val = utils.int_to_bin(num_val)

    bin_string = bin_val.zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: asem_blkw
# Purpose: Takes tokens for .BLKW lines and turns them into their binary
#          equivalent.
# ===============================================================================
def asem_blkw(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    imm5_val = utils.hash_to_int(operand)
    bin_string = ''
    for i in range(0, imm5_val-1):
        bin_string += ''.zfill(MAX_LINE_LENGTH) + '\n'
    bin_string += ''.zfill(MAX_LINE_LENGTH)

    return bin_string

# ================================================================================
# Name: asem_stringz
# Purpose: Takes tokens for .STRINGZ lines and turns them into their binary
#          equivalent.
# ===============================================================================
def asem_stringz(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    bin_string = ''
    for char in operand[1:-1]:
        bin_char = utils.int_to_bin(ord(char)).zfill(MAX_LINE_LENGTH)
        bin_string += bin_char + '\n'
    bin_string += "0000000000000000"
    
    return bin_string

# ===============================================================================
# Name: asem_add
# Purpose: Takes tokens for ADD lines and turns them into their binary
#          equivalent. Uses asem_add_or_and.
# ===============================================================================
def asem_add(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_add_or_and(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_and
# Purpose: Takes tokens for AND lines and turns them into their binaryF
#          equivalent. Uses asem_add_or_and.
# ===============================================================================
def asem_and(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_add_or_and(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_jmp
# Purpose: Takes tokens for JMP lines and turns them into their binary
#          equivalent. Uses asem_jmp_or_jsrr.
# ===============================================================================
def asem_jmp(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_jmp_or_jsrr(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_jsrr
# Purpose: Takes tokens for JSRR lines and turns them into their binary
#          equivalent. Uses asem_jmp_or_jsrr.
# ===============================================================================
def asem_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_jmp_or_jsrr(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_ld
# Purpose: Takes tokens for LD lines and turns them into their binary
#          equivalent. Uses asem_ld_ldi_lea.
# ===============================================================================
def asem_ld(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_ldi
# Purpose: Takes tokens for LDI lines and turns them into their binary
#          equivalent. Uses asem_ld_ldi_lea.
# ===============================================================================
def asem_ldi(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_ldr
# Purpose: Takes tokens for LDR lines and turns them into their binary
#          equivalent. Uses asem_ldr_str.
# ===============================================================================
def asem_ldr(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_ldr_str(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_lea
# Purpose: Takes tokens for LEA lines and turns them into their binary
#          equivalent. Uses asem_ld_ldi_lea.
# ===============================================================================
def asem_lea(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_ld_ldi_lea(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_ret
# Purpose: RET only ever has one binary translation. Simply returns that
#          binary string.
# ===============================================================================
def asem_ret(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RET_BIN_STRING

# ===============================================================================
# Name: asem_rti
# Purpose: RTI only ever has one binary translation. Simply returns that
#          binary string.
# ===============================================================================
def asem_rti(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RTI_BIN_STRING

# ===============================================================================
# Name: asem_st
# Purpose: Takes tokens for ST lines and turns them into their binary
#          equivalent. Uses asem_st_sti.
# ===============================================================================
def asem_st(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_st_sti(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_sti
# Purpose: Takes tokens for STI lines and turns them into their binary
#          equivalent. Uses asem_st_sti.
# ===============================================================================
def asem_sti(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_st_sti(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_str
# Purpose: Takes tokens for STR lines and turns them into their binary
#          equivalent. Uses asem_ldr_str.
# ===============================================================================
def asem_str(address: str, tokens: dict, label_lookup: dict) -> str:
    return asem_ldr_str(address, tokens, label_lookup)

# ===============================================================================
# Name: asem_end
# Purpose: END has no binary translation. Simply returns a blank string
# ===============================================================================
def asem_end(address: str, tokens: dict, label_lookup: dict) -> str:
    return ''


# asem_DICT is used to map all opcode tokens to their respective parsing functions
asem_DICT = {
    'BR'   : asem_br,
    'BRn'  : asem_br,
    'BRz'  : asem_br,
    'BRp'  : asem_br,
    'BRnz' : asem_br,
    'BRnp' : asem_br,
    'BRzp' : asem_br,
    'BRnzp': asem_br,

    'BR'   : asem_br,
    'BRN'  : asem_br,
    'BRZ'  : asem_br,
    'BRP'  : asem_br,
    'BRNZ' : asem_br,
    'BRNP' : asem_br,
    'BRZP' : asem_br,
    'BRNZP': asem_br,

    'ADD' : asem_add,
    'LD'  : asem_ld,
    'ST'  : asem_st,
    'JSR' : asem_jsr,
    'JSRR': asem_jsrr,
    'AND' : asem_and,
    'LDR' : asem_ldr,
    'STR' : asem_str,
    'RTI' : asem_rti,
    'NOT' : asem_not,
    'LDI' : asem_ldi,
    'STI' : asem_sti,
    'JMP' : asem_jmp,
    'RET' : asem_ret,
    'LEA' : asem_lea,

    'TRAP': asem_trap,
    'GETC': asem_explicit_trap,
    'OUT' : asem_explicit_trap,
    'PUTS': asem_explicit_trap,
    'PUTSP': asem_explicit_trap,
    'IN'  : asem_explicit_trap,
    'HALT': asem_explicit_trap,

    '.ORIG': asem_orig,
    '.END' : asem_end,
    '.FILL': asem_fill,
    '.BLKW': asem_blkw,
    '.STRINGZ': asem_stringz
}    