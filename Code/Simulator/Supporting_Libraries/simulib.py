from . import utils
from . import disaslib
from ..Assembler import LC3_Assembler
def create_simulation(machine_code: str) -> str:
    simulation = ''
    for line in machine_code:
        binary = line
        hex = utils.hex_to_int(line)
        #todo add asm
        simulation += f"{binary}\t{hex}\n"
        
    return simulation

def get_cc(operation):
    if operation > 0:
        cc = "P"
    elif operation == 0:
        cc = "Z"
    else:
        cc = "N"
    return cc

def simu_add(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    sr = bin_instruction[7:10]
    mode = bin_instruction[10]
    if mode == 0:
        operand3 = bin_instruction[13:]
        operation = machine_state.registers[SIMU_REGISTERS_DICT[sr]] \
                    + machine_state.registers[SIMU_REGISTERS_DICT[operand3]]
        machine_state.registers[SIMU_REGISTERS_DICT[dr]] = operation

    else:
        operand3 = bin_instruction[11:]
        operation = machine_state.registers[SIMU_REGISTERS_DICT[sr]] \
                    + utils.bin_to_int(operand3)

    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = operation
    machine_state.registers['CC'] = get_cc(operation)
    machine_state.registers['PC'] += 1
    
    return machine_state

def simu_and(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    sr = bin_instruction[7:10]
    mode = bin_instruction[10]
    if mode == 0:
        operand3 = bin_instruction[13:]
        operation = machine_state.registers[SIMU_REGISTERS_DICT[sr]] \
                    & machine_state.registers[SIMU_REGISTERS_DICT[operand3]]
    else:
        operand3 = bin_instruction[11:]
        operation = machine_state.registers[SIMU_REGISTERS_DICT[sr]] \
                    & utils.bin_to_int(operand3)
        
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = operation
    machine_state.registers['CC'] = get_cc(operation)
    machine_state.registers['PC'] += 1
    
    return machine_state

def simu_br(machine_state: object, bin_instruction: str) -> object:
    nzp_string = utils.get_nzp_asm_string(bin_instruction[4:7])
    offset = bin_instruction[7:]
    
    if 'n' in nzp_string and machine_state.registers['CC'] == 'N':
        machine_state.registers['PC'] += utils.twos_complement_to_integer(offset) + 1
    elif 'z' in nzp_string and machine_state.registers['CC'] == 'Z':
        machine_state.registers['PC'] += utils.twos_complement_to_integer(offset) + 1
    elif 'p' in nzp_string and machine_state.registers['CC'] == 'P':
        machine_state.registers['PC'] += utils.twos_complement_to_integer(offset) + 1
    else:
        machine_state.registers['PC'] += 1
    return machine_state
    
def simu_jmp(machine_state: object, bin_instruction: str) -> object:
    base_reg = bin_instruction[7:10]
    machine_state.registers['PC'] = machine_state.registers[SIMU_REGISTERS_DICT[base_reg]]
    return machine_state

def simu_jsr_or_jsrr(machine_state: object, bin_instruction: str) -> object:
    mode = bin_instruction[4]
    machine_state.registers['R7'] = machine_state.registers['PC']
    
    # JSR
    if mode == '1':
        offset = bin_instruction[5:]
        machine_state.registers['PC'] += utils.twos_complement_to_integer(offset) + 1
    # JSRR
    else:
        base_reg = bin_instruction[7:10]
        machine_state.registers['PC'] = machine_state.registers[SIMU_REGISTERS_DICT[base_reg]]
    
    return machine_state

def simu_ld(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    offset = bin_instruction[7:]
    
    pc_offset_address = utils.int_to_hex(machine_state.registers['PC'] + utils.twos_complement_to_integer(offset) + 1)
    
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = utils.bin_to_int(machine_state.memory_space[pc_offset_address][0])
    
    machine_state.registers['PC'] += 1
    
    return machine_state
    

SIMU_FIXED_OPCODE_DICT = {
    utils.RET_BIN_STRING : 'RET',
    utils.RTI_BIN_STRING : 'RTI',
    utils.int_to_bin(utils.TRAPS['GETC']).zfill(16) : 'HALT',
    utils.int_to_bin(utils.TRAPS['OUT']).zfill(16): 'OUT',
    utils.int_to_bin(utils.TRAPS['PUTS']).zfill(16) : 'PUTS',
    utils.int_to_bin(utils.TRAPS['IN']).zfill(16) : 'IN',
    utils.int_to_bin(utils.TRAPS['PUTSP']).zfill(16) : 'PUTSP',
    utils.int_to_bin(utils.TRAPS['HALT']).zfill(16) : 'HALT',
}

SIMU_DYNAMIC_OPCODE_DICT = {
    utils.int_to_bin(utils.OPCODE['BR']).zfill(4) : simu_br,
    utils.int_to_bin(utils.OPCODE['ADD']).zfill(4) : simu_add,
    utils.int_to_bin(utils.OPCODE['AND']).zfill(4) : simu_and,   
    utils.int_to_bin(utils.OPCODE['LD']).zfill(4) : simu_ld,
    utils.int_to_bin(utils.OPCODE['ST']).zfill(4) : 'ST',
    utils.int_to_bin(utils.OPCODE['JSR']).zfill(4) : simu_jsr_or_jsrr,
    utils.int_to_bin(utils.OPCODE['LDR']).zfill(4) : 'LDR',
    utils.int_to_bin(utils.OPCODE['STR']).zfill(4) : 'STR',
    utils.int_to_bin(utils.OPCODE['NOT']).zfill(4) : 'NOT',
    utils.int_to_bin(utils.OPCODE['LDI']).zfill(4) : 'LDI',
    utils.int_to_bin(utils.OPCODE['STI']).zfill(4) : 'STI',
    utils.int_to_bin(utils.OPCODE['JMP']).zfill(4) : simu_jmp,
    utils.int_to_bin(utils.OPCODE['RES']).zfill(4) : 'RES',
    utils.int_to_bin(utils.OPCODE['LEA']).zfill(4) : 'LEA',
    utils.int_to_bin(utils.OPCODE['TRAP']).zfill(4) : 'TRAP'
}

SIMU_REGISTERS_DICT = {
    utils.int_to_bin(utils.REGISTERS['R0']).zfill(3) : 'R0',
    utils.int_to_bin(utils.REGISTERS['R1']).zfill(3) : 'R1',
    utils.int_to_bin(utils.REGISTERS['R2']).zfill(3) : 'R2',
    utils.int_to_bin(utils.REGISTERS['R3']).zfill(3) : 'R3',
    utils.int_to_bin(utils.REGISTERS['R4']).zfill(3) : 'R4',
    utils.int_to_bin(utils.REGISTERS['R5']).zfill(3) : 'R5',
    utils.int_to_bin(utils.REGISTERS['R6']).zfill(3) : 'R6',
    utils.int_to_bin(utils.REGISTERS['R7']).zfill(3) : 'R7'
}