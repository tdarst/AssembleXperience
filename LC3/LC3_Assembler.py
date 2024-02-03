import parselib
import utils
import types

KEY_OPCODE = utils.KEY_OPCODE
KEY_OPERANDS = utils.KEY_OPERANDS
KEY_LABELS = utils.KEY_LABELS

def pass1(code_to_parse: str) -> dict:

    # Program Counter defaults to starting at 0
    address_counter = 0x0

    symbol_table = {
        # address : {opcode : opcode (ops, pseudoOps, dots, etc.),
        #            operands : [registers, labels, strings, etc.] 
        #            labels: [label1, label2, etc.]}
    }

    label_lookup = {}

    solo_label = None
    
    # Gets rid of tabs and newlines
    for line in code_to_parse.replace("\t", " ").split("\n"):
        
        # Gets rid of comments
        line = line.split(";")[0].strip()

        # Get parts of line as a list of tokens
        tokens = line.replace(',','').split(' ')

        # If line is blank
        if not line:
            continue

        # Start address counter at .ORIG
        elif '.ORIG' in line:
            # add .ORIG to symbol table
            address_counter = int(line.split(' ')[1], 16)

        # If .END is reached then break
        elif '.END' in line:
            break

        # If label is solo
        elif tokens[0] is tokens[-1] \
            and tokens[0] not in utils.overall_dictionary:
            solo_label = tokens[0]

        # Any other line
        else:
            # Get parts of line as a list of tokens
            tokens = line.replace(',','').split(' ')

            # If there is a solo label in the last line, add it to the current
            if solo_label:
                tokens.insert(0, solo_label)
                solo_label = None

            # Find the opcode, save it's name and it's index so it can be used as a dividing line for parsing
            find_opcode = next(((token, tokens.index(token)) for token in tokens if token in utils.opcode_dictionary))
            opcode = find_opcode[0]
            opcode_index = find_opcode[1]

            # Operands are all tokens occurring after the opcode,
            # Labels are all tokens occurring before the opcode
            operands = [token for token in tokens[opcode_index+1:]]
            labels   = [token for token in tokens[:opcode_index]]

            # Create a key value pair of the hex'd address and the tokens in the line.
            address = hex(address_counter)
            symbol_table[address] = {
                KEY_OPCODE : opcode,
                KEY_OPERANDS : operands,
                KEY_LABELS : labels
            }

            if labels:
                for label in labels:
                    label_lookup.update({label : address})
            
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

    symbol_table, label_lookup = runPass1()
    print(pass2(symbol_table, label_lookup))
    
    #unitTest_Assembly_Test(runBothPasses())

main()