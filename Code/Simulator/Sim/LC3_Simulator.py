from ..Supporting_Libraries import simulib, utils
from ..Assembler import LC3_Assembler

class MachineState:
    def __init__(self, addressed_instructions, label_lookup, create_with_random=False) -> None:
        self.registers = self.__init_state(create_with_random)
        self.memory_space = self.init_memory_space()
        self.write_instructions_to_memory_space(addressed_instructions)
        self.label_lookup = label_lookup
        self.console_output = ""
        self.running = True
        
    def __init_state(self, create_with_random: bool) -> dict:
        if create_with_random:
            registers = {
                "R0" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R1" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R2" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R3" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R4" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R5" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R6" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "R7" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "PC" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "IR" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "PSR" : utils.get_random_number(utils.FOUR_DIG_HEX_MIN, utils.FOUR_DIG_HEX_MAX),
                "CC" : 'Z'
            }
        else:
            registers = {
                "R0" : 0,
                "R1" : 0,
                "R2" : 0,
                "R3" : 0,
                "R4" : 0,
                "R5" : 0,
                "R6" : 0,
                "R7" : 0,
                "PC" : 0,
                "IR" : 0,
                "PSR" : 0,
                "CC" : 'Z'
            }
        return registers
    
    def init_memory_space(self) -> dict:
        memory_space = {utils.int_to_hex(key): [] for key in range(0x0000, 0x8000 + 1)}
        return memory_space
    
    def write_instructions_to_memory_space(self, addressed_instructions: dict) -> None:
        self.registers['PC'] = utils.hex_to_int(list(addressed_instructions.keys())[0])
        for key in addressed_instructions.keys():
            self.memory_space[key] += addressed_instructions[key]

def decode_obj2(obj2_file_path: str) -> tuple[list, list]:
    bin_ins = []
    asm_ins = []
    obj2_contents = utils.read_from_file(obj2_file_path)
    ins_list = obj2_contents.split('\n')
    for instruction in ins_list:
        bin, asm = instruction.split(":")
        bin_ins.append(bin)
        asm_ins.append(asm)
    return bin_ins, asm_ins

def address_instructions(bin_ins: list, asm_ins: list) -> dict:
    addressed_instructions = {}
    pc = utils.bin_to_int(bin_ins[0])
    included_bin_instructions = bin_ins[1:]
    included_asm_instructions = asm_ins[1:]
    for bin, asm in zip(included_bin_instructions, included_asm_instructions):
        address = utils.int_to_hex(pc)
        addressed_instructions[address] = [bin, asm]
        pc += 1
    return addressed_instructions
        

def add_numbers_to_instructions(addressed_instructions: dict, binary_instructions: list) -> dict:
    # Slices off .END instruction
    binary_instructions = binary_instructions[1:]
    keys = list(addressed_instructions.keys())
    for index, key in enumerate(keys):
        addressed_instructions[key].insert(0, binary_instructions[index])
    return addressed_instructions
        
        
def create_simulation(obj2_file_path: str, create_with_random=False) -> MachineState:
    binary_ins, asm_ins = decode_obj2(obj2_file_path)
    addressed_instructions = address_instructions(binary_ins, asm_ins)
    
    machine_state = MachineState(addressed_instructions, create_with_random)
    
    return machine_state
    
def step_over(machine_state: MachineState) -> MachineState:
    program_counter_key = machine_state.registers['PC']
    memory_content = machine_state.memory_space[utils.int_to_hex(program_counter_key)]
    bin_instruction = memory_content[0] if memory_content else None
    
    if bin_instruction:
        if bin_instruction not in simulib.SIMU_FIXED_OPCODE_DICT:
            opcode = bin_instruction[:4]
            machine_state = simulib.SIMU_DYNAMIC_OPCODE_DICT[opcode](machine_state, bin_instruction)
        else:
            opcode = bin_instruction
            machine_state = simulib.SIMU_FIXED_OPCODE_DICT[opcode](machine_state, bin_instruction)
    
    return machine_state
    
    
    