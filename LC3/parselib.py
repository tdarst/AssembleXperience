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

    bin_string = bin_opcode + bin_OP1 + bin_OP2

    if utils.is_register(OP3):
        OP3 = utils.int_to_bin(utils.REGISTERS[OP3]).zfill(6)
        bin_string += OP3

    elif utils.is_imm5(OP3):
        bin_OP3 = utils.imm5_to_bin(OP3)
        bin_string += '1' + bin_OP3

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

def parse_ld(tokens: dict, label_lookup: dict) -> str: pass

def parse_ldi(tokens: dict, label_lookup: dict) -> str: pass

def parse_ldr(tokens: dict) -> str: pass

def parse_lea(tokens: dict, label_lookup: dict) -> str: pass

def parse_not(tokens: dict) -> str: pass

def parse_ret(tokens: dict) -> str: pass

def parse_rti(tokens: dict) -> str: pass

def parse_st(tokens: dict, label_lookup: dict) -> str: pass

def parse_sti(tokens: dict, label_lookup: dict) -> str: pass

def parse_str(tokens: dict) -> str: pass

def parse_trap(tokens: dict) -> str: pass

def parse_explicit_trap(trap_vector: int) -> str:
    return utils.binary(trap_vector).zfill(MAX_LINE_LENGTH)

def parse_orig(tokens: dict) -> str: pass

def parse_fill(address: str, tokens: dict, label_lookup: dict) -> str:
    # TODO: ADD VALIDATION
    operands = tokens[KEY_OPERANDS]
    imm5_val = operands[0]
    bin_val = utils.int_to_bin(utils.imm5_to_int(imm5_val))
    return bin_val.zfill(MAX_LINE_LENGTH)

def parse_blkw(tokens: dict) -> str: pass

def parse_stringz(tokens: dict) -> str: pass

def parse_end(tokens: dict) -> str:
    return utils.to_bin(0).zfill(MAX_LINE_LENGTH)



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