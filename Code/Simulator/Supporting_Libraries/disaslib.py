from . import utils
# import utils
def build_asm_string(opcode='', opr1='', opr2='', opr3='') -> str:
    opr1_string = f" {opr1}"
    opr2_string = f", {opr2}"
    opr3_string = f", {opr3}"
    return opcode + opr1_string + opr2_string + opr3_string

def disas_add_and(bin_string: str) -> str:
    asm_string = ''
    opcode = DISAS_DYNAMIC_OPCODE_DICT[bin_string[0:4]]
    
    mode = bin_string[10]
    if mode == '0':
        dr = DISAS_REGISTER_DICT[bin_string[4:7]]
        sr1 = DISAS_REGISTER_DICT[bin_string[7:10]]
        sr2 = DISAS_REGISTER_DICT[bin_string[13:]]
        asm_string = build_asm_string(opcode, dr, sr1, sr2)
    
    else:
        dr = DISAS_REGISTER_DICT[bin_string[4:7]]
        sr1 = DISAS_REGISTER_DICT[bin_string[7:10]]
        imm5 = utils.bin_to_hash(bin_string[13:])
        asm_string = build_asm_string(opcode, dr, sr1, imm5)
        
    return asm_string

def disas_br(bin_string: str) -> str: pass

def disas_add(bin_string: str) -> str:
    return disas_add_and(bin_string)
    
def disas_and(bin_string: str) -> str:
    return disas_add_and(bin_string)
        
def disas_br(bin_string: str) -> str: pass
def disas_jmp(bin_string: str) -> str: pass
def disas_jsr(bin_string: str) -> str: pass
def disas_jsrr(bin_string: str) -> str: pass
def disas_ld(bin_string: str) -> str: pass
def disas_ldi(bin_string: str) -> str: pass
def disas_ldr(bin_string: str) -> str: pass
def disas_lea(bin_string: str) -> str: pass
def disas_not(bin_string: str) -> str: pass
def disas_st(bin_string: str) -> str: pass
def disas_sti(bin_string: str) -> str: pass
def disas_str(bin_string: str) -> str: pass
def disas_trap(bin_string: str) -> str: pass

DISAS_FIXED_OPCODE_DICT = {
    utils.RET_BIN_STRING : 'RET',
    utils.RTI_BIN_STRING : 'RTI',
    utils.int_to_bin(utils.TRAPS['GETC']).zfill(16) : 'HALT',
    utils.int_to_bin(utils.TRAPS['OUT']).zfill(16): 'OUT',
    utils.int_to_bin(utils.TRAPS['PUTS']).zfill(16) : 'PUTS',
    utils.int_to_bin(utils.TRAPS['IN']).zfill(16) : 'IN',
    utils.int_to_bin(utils.TRAPS['PUTSP']).zfill(16) : 'PUTSP',
    utils.int_to_bin(utils.TRAPS['HALT']).zfill(16) : 'HALT',
}

DISAS_DYNAMIC_OPCODE_DICT = {
    utils.int_to_bin(utils.OPCODE['BR']).zfill(4) : 'BR',
    utils.int_to_bin(utils.OPCODE['BRn']).zfill(4) : 'BRn',
    utils.int_to_bin(utils.OPCODE['BRz']).zfill(4) : 'BRz',
    utils.int_to_bin(utils.OPCODE['BRp']).zfill(4) : 'BRp',
    utils.int_to_bin(utils.OPCODE['BRnz']).zfill(4) : 'BRnz',
    utils.int_to_bin(utils.OPCODE['BRnp']).zfill(4) : 'BRnp',
    utils.int_to_bin(utils.OPCODE['BRzp']).zfill(4) : 'BRzp',
    utils.int_to_bin(utils.OPCODE['BRnzp']).zfill(4) : 'BRnzp',
    utils.int_to_bin(utils.OPCODE['BRN']).zfill(4) : 'BRN',
    utils.int_to_bin(utils.OPCODE['BRZ']).zfill(4) : 'BRZ',
    utils.int_to_bin(utils.OPCODE['BRP']).zfill(4) : 'BRP',
    utils.int_to_bin(utils.OPCODE['BRNZ']).zfill(4) : 'BRNZ',
    utils.int_to_bin(utils.OPCODE['BRNP']).zfill(4) : 'BRNP',
    utils.int_to_bin(utils.OPCODE['BRZP']).zfill(4) : 'BRZP',
    utils.int_to_bin(utils.OPCODE['BRNZP']).zfill(4) : 'BRNZP',
    utils.int_to_bin(utils.OPCODE['ADD']).zfill(4) : 'ADD',
    utils.int_to_bin(utils.OPCODE['AND']).zfill(4) : 'AND',   
    utils.int_to_bin(utils.OPCODE['LD']).zfill(4) : 'LD',
    utils.int_to_bin(utils.OPCODE['ST']).zfill(4) : 'ST',
    utils.int_to_bin(utils.OPCODE['JSR']).zfill(4) : 'JSR',
    utils.int_to_bin(utils.OPCODE['JSRR']).zfill(4) : 'JSRR',
    utils.int_to_bin(utils.OPCODE['LDR']).zfill(4) : 'LDR',
    utils.int_to_bin(utils.OPCODE['STR']).zfill(4) : 'STR',
    utils.int_to_bin(utils.OPCODE['NOT']).zfill(4) : 'NOT',
    utils.int_to_bin(utils.OPCODE['LDI']).zfill(4) : 'LDI',
    utils.int_to_bin(utils.OPCODE['STI']).zfill(4) : 'STI',
    utils.int_to_bin(utils.OPCODE['JMP']).zfill(4) : 'JMP',
    utils.int_to_bin(utils.OPCODE['RES']).zfill(4) : 'RES',
    utils.int_to_bin(utils.OPCODE['LEA']).zfill(4) : 'LEA',
    utils.int_to_bin(utils.OPCODE['TRAP']).zfill(4) : 'TRAP'
}

DISAS_REGISTER_DICT = {
    utils.int_to_bin(utils.REGISTERS['R0']).zfill(3) : 'R0',
    utils.int_to_bin(utils.REGISTERS['R1']).zfill(3) : 'R1',
    utils.int_to_bin(utils.REGISTERS['R2']).zfill(3) : 'R2',
    utils.int_to_bin(utils.REGISTERS['R3']).zfill(3) : 'R3',
    utils.int_to_bin(utils.REGISTERS['R4']).zfill(3) : 'R4',
    utils.int_to_bin(utils.REGISTERS['R5']).zfill(3) : 'R5',
    utils.int_to_bin(utils.REGISTERS['R6']).zfill(3) : 'R6',
    utils.int_to_bin(utils.REGISTERS['R7']).zfill(3) : 'R7'
}

if __name__ == "__main__":
    print(disas_add('0001001001100001'))