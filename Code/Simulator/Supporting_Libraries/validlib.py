from . import utils

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

ERROR_RETURN_TO_ASSEMBLER = lambda line, line_contents, error: f"*** ERROR <line {line}> ***\nLine: {line_contents}\n{error}"

ERROR_OPCODE_INVALID_OPCODE = lambda given_op: f"Opcode {given_op} does not exist"

ERROR_OPERAND_TYPE_STR = lambda op: f"Invalid operand {op}"
ERROR_OPERAND_LENGTH_STR = lambda req_len, op_len : f"Requires {req_len} operands, but {op_len} given"
ERROR_OPERAND_INVALID_LABEL = lambda label: f"Label {label} is invalid"
ERROR_OPERAND_INVALID_TRAP_VECTOR = lambda vector: f"Trap vector {vector} is invalid"
ERROR_OPERAND_VALUE_OUT_OF_RANGE = lambda value, range: f"Value {value} not in {range}"
ERROR_OPERAND_INVALID_STRING_NOT_ENCLOSED = "Invalid string given"
ERROR_OPERAND_INVALID_STRING_LENGTH = lambda length, range: f"String length {length} not in {range}"

# ===============================================================================
# Name: validate_add_and
# Purpose: Determines whether line is a valid use of ADD or AND. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_add_and(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 3

    if ops_len == req_ops_len:
        OP1 = operands[0]
        OP2 = operands[1]
        OP3 = operands[2]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)
        
        elif not utils.is_register(OP2):
            error_str = ERROR_OPERAND_TYPE_STR(OP2)

        elif not (utils.is_register(OP3) or utils.is_imm5(OP3)):
            error_str = ERROR_OPERAND_TYPE_STR(OP3)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str
    
# ===============================================================================
# Name: valid_jmp_jsrr
# Purpose: Determines whether line is a valid use of JMP or JSRR. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_jmp_jsrr(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_ld_ldi_lea
# Purpose: Determines whether line is a valid use of LD or LADI OR LEA. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_ld_ldi_lea(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 2

    if ops_len == req_ops_len:
        OP1 = operands[0]
        OP2 = operands[1]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)
        
        elif not utils.is_label(OP2, label_lookup):
            error_str = ERROR_OPERAND_INVALID_LABEL(OP2)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_ldr_str
# Purpose: Determines whether line is a valid use of LDR OR STR. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_ldr_str(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 3

    if ops_len == req_ops_len:
        OP1 = operands[0]
        OP2 = operands[1]
        OP3 = operands[2]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)
        
        elif not utils.is_register(OP2):
            error_str = ERROR_OPERAND_TYPE_STR(OP2)

        elif not utils.is_offset6(OP3):
            error_str = ERROR_OPERAND_TYPE_STR(OP3)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_st_sti
# Purpose: Determines whether line is a valid use of ST OR STI. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_st_sti(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 2

    if ops_len == req_ops_len:
        OP1 = operands[0]
        OP2 = operands[1]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)
        
        elif not utils.is_label(OP2, label_lookup):
            error_str = ERROR_OPERAND_INVALID_LABEL(OP2)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ================================================================================
# Name: valid_ret_rti_end_explicit_trap
# Purpose: Determines whether line is a valid use of RET, RTI, or an explicit trap
#          call. Checks forindividual operand errors as well as number of operands
# ================================================================================
def valid_ret_rti_end_explicit_trap(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    req_ops_len = 0
    if operands:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, len(operands))
    
    return error_str

# ===============================================================================
# Name: valid_jsr_br
# Purpose: Determines whether line is a valid use of JSR OR BR. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_jsr_br(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]

        if not utils.is_label(OP1, label_lookup):
            error_str = ERROR_OPERAND_INVALID_LABEL(OP1)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_not
# Purpose: Determines whether line is a valid use of NOT. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_not(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 2

    if ops_len == req_ops_len:
        OP1 = operands[0]
        OP2 = operands[1]

        if not utils.is_register(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)
        
        elif not utils.is_register(OP2):
            error_str = ERROR_OPERAND_TYPE_STR(OP2)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str 

# ===============================================================================
# Name: valid_trap
# Purpose: Determines whether line is a valid use of TRAP. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_trap(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]
        
        if not utils.is_hex(OP1):
            error_str = ERROR_OPERAND_INVALID_TRAP_VECTOR(OP1)
            
        elif not utils.hex_to_int(OP1) in utils.TRAPS.values():
            error_str = ERROR_OPERAND_INVALID_TRAP_VECTOR(OP1)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_orig
# Purpose: Determines whether line is a valid use of ORIG. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_orig(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]

        if not utils.is_hex(OP1):
            error_str = ERROR_OPERAND_TYPE_STR(OP1)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_fill
# Purpose: Determines whether line is a valid use of FILL. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_fill(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]

        type_conditions = [
            utils.is_hex(OP1),
            utils.is_hash(OP1),
            utils.is_bin(OP1)
        ]

        if sum(type_conditions) == 0:
            error_str = ERROR_OPERAND_TYPE_STR(OP1)

        elif not utils.is_imm16(OP1):
            error_str = ERROR_OPERAND_VALUE_OUT_OF_RANGE(OP1, utils.IMM16_INT_RANGE)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_blkw
# Purpose: Determines whether line is a valid use of BLKW. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_blkw(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    ops_len = len(operands)
    req_ops_len = 1

    if ops_len == req_ops_len:
        OP1 = operands[0]

        type_conditions = [
            utils.is_hex(OP1),
            utils.is_hash(OP1),
            utils.is_bin(OP1)
        ]

        if sum(type_conditions) == 0:
            error_str = ERROR_OPERAND_TYPE_STR(OP1)

        elif not utils.is_blkw_valid_val(OP1):
            error_str = ERROR_OPERAND_VALUE_OUT_OF_RANGE(OP1, utils.BLKW_INT_RANGE)

    else:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, ops_len)

    return error_str

# ===============================================================================
# Name: valid_stringz
# Purpose: Determines whether line is a valid use of STRINGZ. Checks for
#          individual operand errors as well as number of operands
# ===============================================================================
def valid_stringz(tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    operands = tokens[KEY_OPERANDS]
    given_str = ' '.join(operands) if operands else None
    req_ops_len = 1

    if not (operands[0].startswith('"') and operands[-1].endswith('"')):
        error_str = ERROR_OPERAND_INVALID_STRING_NOT_ENCLOSED

    elif not given_str:
        error_str = ERROR_OPERAND_LENGTH_STR(req_ops_len, 0)

    elif not utils.in_range(len(given_str), utils.STRINGZ_INT_RANGE):
        error_str = ERROR_OPERAND_INVALID_STRING_LENGTH(len(given_str), utils.STRINGZ_INT_RANGE)

    return error_str

# ===============================================================================
# Name: valid_add
# Purpose: Uses combined validation function valid_add_and to validate.
# ===============================================================================
def valid_add(tokens: dict, label_lookup: dict) -> str:
    return valid_add_and(tokens, label_lookup)

# ===============================================================================
# Name: valid_and
# Purpose: Uses combined validation function valid_add_and to validate.
# ===============================================================================
def valid_and(tokens: dict, label_lookup: dict) -> str:
    return valid_add_and(tokens, label_lookup)

# ===============================================================================
# Name: valid_jmp
# Purpose: Uses combined validation function valid_jmp_jsrr to validate.
# ===============================================================================
def valid_jmp(tokens: dict, label_lookup: dict) -> str:
    return valid_jmp_jsrr(tokens, label_lookup)

# ===============================================================================
# Name: valid_jsrr
# Purpose: Uses combined validation function valid_jmp_jsrr to validate.
# ===============================================================================
def valid_jsrr(tokens: dict, label_lookup: dict) -> str:
    return valid_jmp_jsrr(tokens, label_lookup)

# ===============================================================================
# Name: valid_jsr
# Purpose: Uses combined validation function valid_jsr_br to validate.
# ===============================================================================
def valid_jsr(tokens: dict, label_lookup: dict) -> str:
    return valid_jsr_br(tokens, label_lookup)

# ===============================================================================
# Name: valid_br
# Purpose: Uses combined validation function valid_jsr_br to validate.
# ===============================================================================
def valid_br(tokens: dict, label_lookup: dict) -> str:
    return valid_jsr_br(tokens, label_lookup)

# ===============================================================================
# Name: valid_ld
# Purpose: Uses combined validation function valid_ld_ldi_lea to validate.
# ===============================================================================
def valid_ld(tokens: dict, label_lookup: dict) -> str:
    return valid_ld_ldi_lea(tokens, label_lookup)

# ===============================================================================
# Name: valid_ldi
# Purpose: Uses combined validation function valid_ld_ldi_lea to validate.
# ===============================================================================
def valid_ldi(tokens: dict, label_lookup: dict) -> str:
    return valid_ld_ldi_lea(tokens, label_lookup)

# ===============================================================================
# Name: valid_ldr
# Purpose: Uses combined validation function valid_ldr_str to validate.
# ===============================================================================
def valid_ldr(tokens: dict, label_lookup: dict) -> str:
    return valid_ldr_str(tokens, label_lookup)

# ===============================================================================
# Name: valid_str
# Purpose: Uses combined validation function valid_ldr_str to validate.
# ===============================================================================
def valid_str(tokens: dict, label_lookup: dict) -> str:
    return valid_ldr_str(tokens, label_lookup)

# ===============================================================================
# Name: valid_lea
# Purpose: Uses combined validation function valid_ld_ldi_lea to validate.
# ===============================================================================
def valid_lea(tokens: dict, label_lookup: dict) -> str:
    return valid_ld_ldi_lea(tokens, label_lookup)

# ===============================================================================
# Name: valid_ret
# Purpose: Uses combined validation function valid_ret_rti_end_explicit_trap to 
#          validate.
# ===============================================================================
def valid_ret(tokens: dict, label_lookup: dict) -> str:
    return valid_ret_rti_end_explicit_trap(tokens, label_lookup)

# ===============================================================================
# Name: valid_rti
# Purpose: Uses combined validation function valid_ret_rti_end_explicit_trap to 
#          validate.
# ===============================================================================
def valid_rti(tokens: dict, label_lookup: dict) -> str:
    return valid_ret_rti_end_explicit_trap(tokens, label_lookup)

# ===============================================================================
# Name: valid_explicit_trap
# Purpose: Uses combined validation function valid_ret_rti_end_explicit_trap to 
#          validate.
# ===============================================================================
def valid_explicit_trap(tokens: dict, label_lookup: dict) -> str:
    return valid_ret_rti_end_explicit_trap(tokens, label_lookup)

# ===============================================================================
# Name: valid_end
# Purpose: Uses combined validation function valid_ret_rti_end_explicit_trap to 
#          validate.
# ===============================================================================
def valid_end(tokens: dict, label_lookup: dict) -> str:
    return valid_ret_rti_end_explicit_trap(tokens, label_lookup)

# ===============================================================================
# Name: valid_st
# Purpose: Uses combined validation function valid_st_sti to validate.
# ===============================================================================
def valid_st(tokens: dict, label_lookup: dict) -> str:
    return valid_st_sti(tokens, label_lookup)

# ===============================================================================
# Name: valid_sti
# Purpose: Uses combined validation function valid_st_sti to validate.
# ===============================================================================
def valid_sti(tokens: dict, label_lookup: dict) -> str:
    return valid_st_sti(tokens, label_lookup)
    
# VALID_DICT is used to map all opcode tokens to their respective validation functions
VALID_DICT = {
    'BR'   : valid_br,
    'BRn'  : valid_br,
    'BRz'  : valid_br,
    'BRp'  : valid_br,
    'BRnz' : valid_br,
    'BRnp' : valid_br,
    'BRzp' : valid_br,
    'BRnzp': valid_br,

    'BR'   : valid_br,
    'BRN'  : valid_br,
    'BRZ'  : valid_br,
    'BRP'  : valid_br,
    'BRNZ' : valid_br,
    'BRNP' : valid_br,
    'BRZP' : valid_br,
    'BRNZP': valid_br,

    'ADD' : valid_and,
    'LD'  : valid_ld,
    'ST'  : valid_st,
    'JSR' : valid_jsr_br,
    'JSRR': valid_jsrr,
    'AND' : valid_and,
    'LDR' : valid_ldr,
    'STR' : valid_str,
    'RTI' : valid_rti,
    'NOT' : valid_not,
    'LDI' : valid_ldi,
    'STI' : valid_sti,
    'JMP' : valid_jmp,
    'RET' : valid_ret,
    'LEA' : valid_lea,

    'TRAP': valid_trap,
    'GETC': valid_explicit_trap,
    'OUT' : valid_explicit_trap,
    'PUTS': valid_explicit_trap,
    'PUTSP': valid_explicit_trap,
    'IN'  : valid_explicit_trap,
    'HALT': valid_explicit_trap,

    '.ORIG': valid_orig,
    '.END' : valid_end,
    '.FILL': valid_fill,
    '.BLKW': valid_blkw,
    '.STRINGZ': valid_stringz,
    
}

# ===============================================================================
# Name: assemble_line_contents
# Purpose: Uses tokens to assemble the original written line for error output.
# ===============================================================================
def assemble_line_contents(tokens: dict) -> str:
    label = tokens[KEY_LABELS]
    opcode = tokens[KEY_OPCODE]
    operands = tokens[KEY_OPERANDS]
    line_contents = f"{' '.join(label) if label else ''} {opcode} {' '.join(operands) if operands else ''}"
    return line_contents

# ===============================================================================
# Name: validate_line
# Purpose: Checks if there is an opcode error, if not checks if there's an
#          operand error, otherwise returns empty string.
# ===============================================================================
def validate_line(line: int, tokens: dict, label_lookup: dict) -> str:
    error_str = ''
    line = line
    line_contents = assemble_line_contents(tokens)
    opcode = tokens[KEY_OPCODE]

    valid_func = utils.lookup_all_caps(opcode, VALID_DICT)
    
    if valid_func:
        error = valid_func(tokens, label_lookup)
    else:
        error = ERROR_OPCODE_INVALID_OPCODE(opcode)

    if error:
        error_str = ERROR_RETURN_TO_ASSEMBLER(line, line_contents, error)

    return error_str