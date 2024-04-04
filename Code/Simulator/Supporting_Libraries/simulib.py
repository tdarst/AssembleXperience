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

def get_cc(operation: int) -> str:
    bin_val = utils.int_to_bin(operation).zfill(16)
    if bin_val.startswith('1'):
        operation = utils.twos_complement_to_integer(utils.calc_twos_complement(bin_val))
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
        twos = utils.twos_complement_to_integer(operand3)
        operation = machine_state.registers[SIMU_REGISTERS_DICT[sr]] \
                    + utils.twos_complement_to_integer(operand3)

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
    value_to_load = utils.bin_to_int(machine_state.memory_space[pc_offset_address][0])
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = value_to_load
    machine_state.registers['CC'] = get_cc(value_to_load)
    machine_state.registers['PC'] += 1
    return machine_state

def simu_ldi(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    offset = bin_instruction[7:]
    pc_offset_address = machine_state.registers['PC'] + utils.twos_complement_to_integer(offset) + 1
    pointer = utils.bin_to_int(machine_state.memory_space[utils.int_to_hex(pc_offset_address)][0])
    value_to_load = utils.bin_to_int(machine_state.memory_space[utils.int_to_hex(pointer)][0])
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = value_to_load
    machine_state.registers['CC'] = get_cc(value_to_load)
    machine_state.registers['PC'] += 1
    return machine_state
    
def simu_ldr(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    br = bin_instruction[7:10]
    offset = bin_instruction[10:]
    
    address_to_look = machine_state.registers[SIMU_REGISTERS_DICT[br]] + utils.twos_complement_to_integer(offset)
    value_to_load = utils.bin_to_int(machine_state.memory_space[utils.int_to_hex(address_to_look)][0])
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = value_to_load
    
    machine_state.registers['CC'] = get_cc(value_to_load)
    machine_state.registers['PC'] += 1
    return machine_state

def simu_lea(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    offset = bin_instruction[7:]
    
    pc_offset_address = machine_state.registers['PC'] + utils.twos_complement_to_integer(offset) + 1
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = pc_offset_address
    
    machine_state.registers['CC'] = get_cc(pc_offset_address)
    machine_state.registers['PC'] += 1
    return machine_state

def simu_not(machine_state: object, bin_instruction: str) -> object:
    dr = bin_instruction[4:7]
    sr = bin_instruction[7:10]
    
    operation = utils.not_int(machine_state.registers[SIMU_REGISTERS_DICT[sr]])
    machine_state.registers[SIMU_REGISTERS_DICT[dr]] = operation

    machine_state.registers['CC'] = get_cc(operation)
    machine_state.registers['PC'] += 1
    return machine_state

def simu_st(machine_state: object, bin_instruction: str) -> object:
    sr = bin_instruction[4:7]
    offset = bin_instruction[7:]
    
    pc_offset_val = machine_state.registers['PC'] + utils.bin_to_int(offset) + 1
    sr_val = utils.integer_to_twos_complement(machine_state.registers[SIMU_REGISTERS_DICT[sr]], 16)
    
    try:
        machine_state.memory_space[utils.int_to_hex(pc_offset_val)][0] = sr_val
    except:
        machine_state.memory_space[utils.int_to_hex(pc_offset_val)].append(sr_val)
    machine_state.registers['PC'] += 1
    return machine_state

def simu_sti(machine_state: object, bin_instruction: str) -> object:
    sr = bin_instruction[4:7]
    offset = bin_instruction[7:]

    pc_offset_val = machine_state.registers['PC'] + utils.twos_complement_to_integer(offset) + 1
    sr_val = utils.integer_to_twos_complement(machine_state.registers[SIMU_REGISTERS_DICT[sr]], 16)
    
    address_to_store_in = utils.bin_to_hex(machine_state.memory_space[utils.int_to_hex(pc_offset_val)][0])
    try:
        machine_state.memory_space[address_to_store_in][0] = sr_val
    except:
        machine_state.memory_space[address_to_store_in].append(sr_val)
    
    machine_state.registers['PC'] += 1
    return machine_state

def simu_str(machine_state: object, bin_instruction: str) -> object:
    sr = bin_instruction[4:7]
    br = bin_instruction[7:10]
    offset = bin_instruction[10:]
    
    sr_val = utils.integer_to_twos_complement(machine_state.registers[SIMU_REGISTERS_DICT[sr]], 16)
    offset_val = utils.int_to_hex(machine_state.registers[SIMU_REGISTERS_DICT[br]] + utils.twos_complement_to_integer(offset))
    
    try:
        machine_state.memory_space[offset_val][0] = sr_val
    except:
        machine_state.memory_space[offset_val].append(sr_val)
    
    machine_state.registers['PC'] += 1
    return machine_state

def simu_ret(machine_state: object, bin_instruction: str) -> object:
    machine_state.registers['PC'] = machine_state.registers['R7']
    return machine_state

def simu_out_trapx21(machine_state: object, bin_instruction: str) -> object:
    r0_val = machine_state.registers['R0']
    machine_state.console_output = chr(r0_val)
    # CC is always positive for OUT
    machine_state.registers['CC'] = "P"
    machine_state.registers['PC'] += 1
    # The address following the OUT instruction gets saved in R7
    machine_state.registers['R7'] = machine_state.registers['PC']
    return machine_state

def simu_halt_trapx25(machine_state: object, bin_instruction: str) -> object:
    machine_state.running = False
    return machine_state

def simu_puts_trapx22(machine_state: object, bin_instruction: str) -> object:
    null = False
    address = machine_state.registers['R0']
    while null == False:
        string_address = utils.int_to_hex(address)
        bin_ins = machine_state.memory_space[string_address][0]
        machine_state.console_output += chr(utils.bin_to_int(bin_ins))
        if all(char == '0' for char in bin_ins):
            null = True
        address += 1
    
    machine_state.registers['PC'] += 1
    return machine_state

def simu_putsp_trapx24(machine_state: object, bin_instruction: str) -> object:
    null = False
    address = machine_state.registers['R0']
    while null == False:
        string_address = utils.int_to_hex(address)
        bin_ins = machine_state.memory_space[string_address][0]
        char1 = bin_ins[8:16]
        char2 = bin_ins[0:8]
        machine_state.console_output += chr(utils.bin_to_int(char1))
        machine_state.console_output += chr(utils.bin_to_int(char2))
        if all(char == '0' for char in bin_ins):
            null = True
        address += 1
    
    machine_state.registers['PC'] += 1
    return machine_state

def simu_getc_trapx20(machine_state: object, bin_instruction: str) -> object:
    machine_state.input_mode = 1
    return machine_state

def simu_in_trapx23(machine_state: object, bin_instruction: str) -> object:
    machine_state.input_mode = 2
    return machine_state

SIMU_FIXED_OPCODE_DICT = {
    utils.RET_BIN_STRING : simu_ret,
    utils.RTI_BIN_STRING : 'RTI',
    "1111000000100000" : simu_getc_trapx20,
    "1111000000100001": simu_out_trapx21,
    "1111000000100010" : simu_puts_trapx22,
    "1111000000100011" : simu_in_trapx23,
    "1111000000100100" : simu_putsp_trapx24,
    "1111000000100101" : simu_halt_trapx25,
}

SIMU_DYNAMIC_OPCODE_DICT = {
    utils.int_to_bin(utils.OPCODE['BR']).zfill(4) : simu_br,
    utils.int_to_bin(utils.OPCODE['ADD']).zfill(4) : simu_add,
    utils.int_to_bin(utils.OPCODE['AND']).zfill(4) : simu_and,   
    utils.int_to_bin(utils.OPCODE['LD']).zfill(4) : simu_ld,
    utils.int_to_bin(utils.OPCODE['ST']).zfill(4) : simu_st,
    utils.int_to_bin(utils.OPCODE['JSR']).zfill(4) : simu_jsr_or_jsrr,
    utils.int_to_bin(utils.OPCODE['LDR']).zfill(4) : simu_ldr,
    utils.int_to_bin(utils.OPCODE['STR']).zfill(4) : simu_str,
    utils.int_to_bin(utils.OPCODE['NOT']).zfill(4) : simu_not,
    utils.int_to_bin(utils.OPCODE['LDI']).zfill(4) : simu_ldi,
    utils.int_to_bin(utils.OPCODE['STI']).zfill(4) : simu_sti,
    utils.int_to_bin(utils.OPCODE['JMP']).zfill(4) : simu_jmp,
    utils.int_to_bin(utils.OPCODE['RES']).zfill(4) : 'RES',
    utils.int_to_bin(utils.OPCODE['LEA']).zfill(4) : simu_lea
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