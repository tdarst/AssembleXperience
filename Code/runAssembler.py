from Simulator.Assembler import LC3_Assembler
import sys
if __name__ == "__main__":
    file_path = sys.argv[1]
    # file_path = r"C:\lc3_assembly_work\chatgptfactorial.asm"
    print(LC3_Assembler.assemble(file_path))
    
    # DEBUG PARSING
    # file_path = r"C:\lc3_assembly_work\chatgptfactorial.asm"
    # with open(file_path,'r') as asm_file:
    #     readLines = asm_file.read()
    # print(LC3_Assembler.ready_code_for_parsing(readLines))