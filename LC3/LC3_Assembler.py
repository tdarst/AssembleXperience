import parselib
import utils
import types

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

def ready_code_for_parsing(code: str) -> str:
    # Get rid of all tabs and split the code into a list seperated by lines
    code_list = code.replace("\t", " ").split("\n")

    # Get rid of all comments left
    code_list_comments_removed = [line.split(";")[0].strip() 
                                  for line in code_list 
                                  if line.split(';')[0]]

    return code_list_comments_removed

def check_if_solo_label(tokens: list) -> str:
    solo_label = None
    if tokens[0] is tokens[-1] and tokens[0] not in utils.overall_dictionary:
        solo_label = tokens[0]
    return solo_label

def find_opcode_in_tokens(tokens: list) -> tuple[str, int]:
    return next((token, tokens.index(token)) for token in tokens if token in utils.opcode_dictionary)

def update_label_lookup(address: str, labels: list, label_lookup: dict) -> dict:
    [label_lookup.update({label:address}) for label in labels if labels]
    return label_lookup

def get_operands(tokens: list, opcode_index: int) -> list:
    return [token for token in tokens[opcode_index+1:]]

def get_labels(tokens: list, opcode_index: int) -> list:
    return [token for token in tokens[:opcode_index]]

def check_for_ORIG(address_counter: int, opcode: str, operands: list) -> tuple[int, bool]:
    if opcode == utils.ORIG_OPCODE_NAME:
        address_counter = utils.hex_to_int(operands[0])
    return address_counter

def pass1(code_to_parse: str) -> tuple[dict, dict]:

    # Program Counter defaults to starting at 0
    address_counter = 0x0

    symbol_table = {
        # address : {opcode : opcode (ops, pseudoOps, dots, etc.),
        #            operands : [registers, labels, strings, etc.] 
        #            labels: [label1, label2, etc.]}
    }

    label_lookup = {
        # label_name : label_address
    }
    
    # Gets rid of tabs and newlines
    for line in ready_code_for_parsing(code_to_parse):
        # Get parts of line as a list of tokens
        tokens = line.replace(',','').split(' ')

        # Check if line is a solo label
        solo_label = check_if_solo_label(tokens)

        # If there is a solo label in the last line, add it to the current
        if solo_label:
            tokens.insert(0, solo_label)
            solo_label = None

        # Find the opcode, save it's name and it's index so it can be used as a dividing line for parsing
        opcode, opcode_index = find_opcode_in_tokens(tokens)

        # Operands are all tokens occurring after the opcode,
        # Labels are all tokens occurring before the opcode
        operands = get_operands(tokens, opcode_index)
        labels   = get_labels(tokens, opcode_index)

        # If .ORIG is in the line then set address_counter to it and don't increment address_counter.
        address_counter = check_for_ORIG(address_counter, opcode, operands)

        # Create a dictionary 
        # Key: line's hex address 
        # Values: token categories.
        address = hex(address_counter)
        symbol_table[address] = {
            KEY_OPCODE : opcode,
            KEY_OPERANDS : operands,
            KEY_LABELS : labels
        }

        # Update label_lookup with any labels
        label_lookup = update_label_lookup(address, labels, label_lookup)
        
        # Increment the address_counter
        address_counter += 0x1

    return symbol_table, label_lookup

def pass2(symbol_table, label_lookup):
    machine_code = ''
    for address, tokens in symbol_table.items():
        opcode = tokens[KEY_OPCODE]
        bin_string = parselib.PARSE_DICT[opcode](address, tokens, label_lookup)
        machine_code += f"{bin_string}\n"

    return machine_code.rstrip('\n')

def main():
    addTest = r'LC3\Test_Code\add_test.txt'
    debugString = r'LC3\Test_Code\Assembly_Test.txt'
    debugString2 = r"LC3\Test_Code\2048.asm"

    path = debugString

    def runBothPasses():
        with open(path, 'r') as file:
            readLines = file.read()
            return pass2(pass1(readLines))

    def runPass1():
        with open(path, 'r') as file:
            readLines = file.read()
            return pass1(readLines)
        
    def runParseCode():
        with open(path, 'r') as file:
            readLines = file.read()
            return ready_code_for_parsing(readLines)

    symbol_table, label_lookup = runPass1()
    print(pass2(symbol_table, label_lookup))
    
    #unitTest_Assembly_Test(runBothPasses())

main()