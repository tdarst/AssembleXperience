import sys
from Scripts.Assembler import LC3_Assembler

# Runs the assembler, takes command line argument as path.
if __name__=='__main__':
    asm_path = r"C:\Users\trevo\OneDrive\Documents\AssemblyStuff\AssemblyFactorial\AssemblyFactorial.asm"
    # asm_path = sys.argv[1]
    LC3_Assembler.main(asm_path)