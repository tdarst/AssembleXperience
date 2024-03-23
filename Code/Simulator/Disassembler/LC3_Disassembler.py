from ..Supporting_Libraries import utils

def ready_machine_code(machine_code: str) -> list:
    machine_code_list = machine_code.split('\n')
    return machine_code_list

def disassemble(machine_code: str) -> str:
    for bin_string in ready_machine_code(machine_code):
        opcode = bin_string[:4]

def main(bin_file_path: str) -> tuple[str, bool]:
    file_contents = utils.read_from_file(bin_file_path)
    