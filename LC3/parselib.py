# Library of functions to parse different lines.
import utils

MAX_LINE_LENGTH = 16
OPCODE_LENGTH = 4
REGISTER_LENGTH = 3

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

def parse_add_or_and(address: str, tokens: dict, label_lookup: dict) -> str:
    #TODO: ADD VALIDATION
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
        bin_OP3 += utils.imm5_to_bin(OP3).zfill(5)

    bin_string = bin_opcode + bin_OP1 + bin_OP2 + bin_OP3

    return bin_string

def parse_jmp_or_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    OP1 = tokens[KEY_OPERANDS][0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    fill_zeros3 = ''.zfill(3)
    bin_reg = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    fill_zeros6 = ''.zfill(6)

    bin_string = bin_opcode + fill_zeros3 + bin_reg + fill_zeros6

    return bin_string

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

def parse_ldr_str(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    OP1, OP2, OP3 = operands[0], operands[1], operands[2]
    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_OP1 = utils.int_to_bin(utils.REGISTERS[OP1]).zfill(REGISTER_LENGTH)
    bin_OP2 = utils.int_to_bin(utils.REGISTERS[OP2]).zfill(REGISTER_LENGTH)

    bin_string = bin_opcode + bin_OP1 + bin_OP2

    if utils.is_imm5(OP3):
        bin_OP3 = utils.imm5_to_bin(OP3).zfill(6)
        bin_string += bin_OP3

    else:
        bin_OP3 = utils.hex_to_bin(OP3).zfill(6)
        bin_string += bin_OP3

    return bin_string


def parse_add(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_add_or_and(address, tokens, label_lookup)

def parse_and(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_add_or_and(address, tokens, label_lookup)

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

def parse_jmp(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_jmp_or_jsrr(address, tokens, label_lookup)
    
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

def parse_jsrr(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_jmp_or_jsrr(address, tokens, label_lookup)

def parse_ld(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

def parse_ldi(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

def parse_ldr(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ldr_str(address, tokens, label_lookup)

def parse_lea(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ld_ldi_lea(address, tokens, label_lookup)

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

def parse_ret(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RET_BIN_STRING

def parse_rti(address: str, tokens: dict, label_lookup: dict) -> str:
    return utils.RTI_BIN_STRING

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


def parse_st(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_st_sti(address, tokens, label_lookup)

def parse_sti(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_st_sti(address, tokens, label_lookup)

def parse_str(address: str, tokens: dict, label_lookup: dict) -> str:
    return parse_ldr_str(address, tokens, label_lookup)

def parse_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    trap_vector = operands[0]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.hex_to_bin(trap_vector).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

def parse_explicit_trap(address: str, tokens: dict, label_lookup: dict) -> str:
    opcode = 'TRAP'
    trap_vector = tokens[KEY_OPCODE]

    bin_opcode = utils.int_to_bin(utils.OPCODE[opcode]).zfill(OPCODE_LENGTH)
    bin_trap = utils.int_to_bin(utils.TRAPS[trap_vector]).zfill(12)

    bin_string = bin_opcode + bin_trap

    return bin_string

def parse_orig(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    hex_val = operands[0]

    bin_string = utils.hex_to_bin(hex_val).zfill(MAX_LINE_LENGTH)

    return bin_string

def parse_fill(address: str, tokens: dict, label_lookup: dict) -> str:
    operands = tokens[KEY_OPERANDS]
    imm5_val = operands[0]
    bin_val = utils.int_to_bin(utils.imm5_to_int(imm5_val))

    bin_string = bin_val.zfill(MAX_LINE_LENGTH)

    return bin_string

def parse_blkw(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    imm5_val = utils.imm5_to_int(operand)
    bin_string = ''
    for i in range(0, imm5_val-1):
        bin_string += ''.zfill(MAX_LINE_LENGTH) + '\n'
    bin_string += ''.zfill(MAX_LINE_LENGTH)

    return bin_string

def parse_stringz(address: str, tokens: dict, label_lookup: dict) -> str:
    operand = tokens[KEY_OPERANDS][0]
    bin_string = ''
    for char in operand:
        bin_char = utils.int_to_bin(ord(char)).zfill(MAX_LINE_LENGTH)
        bin_string += bin_char + '\n'
    bin_string += ''.zfill(MAX_LINE_LENGTH)
    
    return bin_string

def parse_end(address: str, tokens: dict, label_lookup: dict) -> str:
    return ''

PARSE_DICT = {
    'BR'   : parse_br,
    'BRn'  : parse_br,
    'BRz'  : parse_br,
    'BRp'  : parse_br,
    'BRnz' : parse_br,
    'BRnp' : parse_br,
    'BRzp' : parse_br,
    'BRnzp': parse_br,

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