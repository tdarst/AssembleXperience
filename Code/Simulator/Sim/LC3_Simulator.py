from ..Supporting_Libraries import simulib, utils
from ..Assembler import LC3_Assembler

class MachineState:
    def __init__(self, addressed_instructions, label_lookup, create_with_random=False) -> None:
        self.registers = self.__init_state(create_with_random)
        self.memory_space = self.init_memory_space()
        self.write_instructions_to_memory_space(addressed_instructions)
        self.label_lookup = label_lookup
        self.console_output = ""
        
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
        for key in addressed_instructions.keys():
            self.memory_space[key] += addressed_instructions[key]
    
def decode_obj2(obj2_file_path: str) -> tuple[list, list]:
    bytes_string = ""
    with open(obj2_file_path, 'r') as bytes:
        bytes_string=bytes.read()
    decoded_lines = bytes_string.split('\n')
    bin_vals = []
    asm_vals = []

    for i in decoded_lines:
        if utils.is_bin(i):
            bin_vals.append(i)
        else:
            asm_vals.append(i)
    
    return bin_vals, asm_vals

def construct_instructions(symbol_table: dict) -> dict:
    instruction_set = {}
    def get_operand_string(operands: list) -> str:
        operand_string = ""
        if operands:
            for i in range(len(operands)-1):
                operand_string += operands[i] + ", "
            operand_string += operands[-1]
        return operand_string
    
    def get_label_string(labels: list) -> str:
        label_string = ""
        if labels:
            for label in labels:
                label_string += f"{label} "
        return label_string

    instruction_set = {}
    
    for value in symbol_table.values():
        if '.END' not in value['opcode']:
            instruction_set.update({value['address']:[f"{get_label_string(value['labels'])}{value['opcode']} {get_operand_string(value['operands'])}"]})
        
    return instruction_set

def add_numbers_to_instructions(addressed_instructions: dict, binary_instructions: list) -> dict:
    # Slices off .END instruction
    keys = list(addressed_instructions.keys())
    # Slices off .ORIG binary
    # binary_instructions = binary_instructions[1:]
    for index, key in enumerate(keys):
        addressed_instructions[key].insert(0, binary_instructions[index])
    return addressed_instructions
        
        
def create_simulation(obj2_file_path: str, create_with_random=False) -> MachineState:
    binary_ins, asm_ins = decode_obj2(obj2_file_path)
    asm_ins_string = "\n".join(asm_ins)
    symbol_table, label_lookup = LC3_Assembler.pass1(asm_ins_string)
    addressed_instructions = construct_instructions(symbol_table)
    updated_addressed_instructions = add_numbers_to_instructions(addressed_instructions, binary_ins)
    
    machine_state = MachineState(updated_addressed_instructions, label_lookup, create_with_random)
    
    return machine_state
    
    
    