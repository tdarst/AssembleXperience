# Senior Design Project Task List

## Assembler 
- Research all LC-3 instructions and what their binary and non-binary names are.
- Research LC-3 components (i.e. registers, program counters)
- Implement dictionaries containing all LC-3 instructions and registers
- Implement parser to separate LC-3 program into lists of instructions with no white space
- Implement translator to translate the parsed programs into it’s binary equivalent
- Implement function to save this binary equivalent into a text file
- Acquire a lot of long assembly programs to test the assembler on
- Create unit tests for assembler
## Disassembler
- Write up binary to text dictionaries for all LC-3 instructions and registers
- Implement parser to separate binary with whitespace from text file
- Implement function to translate binary to text using dictionaries
- Implement function to save translation to text file
- Acquire a lot of long assembly programs to test the disassembler on
- Create unit tests for disassembler
## ISA Level Simulation
- Implement function to load an assembled program from a text file to simulator
- Implement function to calculate addresses using program counters and offsets
- Implement function to step through each line of code
- Implement GUI consisting of zones to visually hold the program counters and registers
- Implement GUI consisting of zone for code with current line highlighted
- Implement toolbar options for loading and executing programs
