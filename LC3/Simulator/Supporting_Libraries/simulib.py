from . import utils
def create_simulation(machine_code: str) -> str:
    simulation = ''
    for line in machine_code:
        binary = line
        hex = utils.hex_to_int(line)
        #todo add asm
        simulation += f"{binary}\t{hex}\n"
        
    return simulation