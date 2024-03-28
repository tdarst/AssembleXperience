# GETTING STARTED
1. Download any version of Python 3 from [Python's official website](https://www.python.org/downloads/)
2. Make sure pip is installed by running **py -m ensurepip** in command line
3. Clone repository
4. Navigate to repository root directory (should be named Senior_Design)
5. Open root directory in command line
6. Run command **pip install -r requirements.txt** to download all required libraries

# Running the Simulator
1. From the root directory navigate to Code
2. Open the Code directory in command line
3. Run command **python runSimulator.py**

# Navigating the Simulator
### Edit Tab
Text Editor Window
> The Text Editor allows you to write code with very basic editing features like a line counter and color coding.
Console Window
> Below the text editor is a console that will allow the program to talk to you when assembling files, namely
> whether the file was successfully assembled or not and the directory it was assembled to.
Load Button
> The load button allows you to choose a .txt or .asm file to load into the text editor.
Save Button
> The save button allows you to save the contents of your text editor to a file.
Assemble Button
> The assemble button attempts to assemble the file loaded into the text editor to the directory of the loaded file.
> If there are any errors with the assembling process, or if the process is successful, you will be notified in the
> console output. The file output of a successfully assembled file will be in the .obj2 format.

### Simulate Tab
Simulator Window
> The simulator window holds the contents of the simulation inside after you've loaded a .obj2 file.
Console Window
> The console window holds the contents of any input or output as required by the simulator's code.
Registers Window
> The registers window shows the contents of the registers after each instruction in the simulator.
Load Button
> The load button allows you to choose a .obj2 file to load.
Reload File Button
> The reload file button allows you to reload the same file and reset the machine settings.
Run Button
> The run button runs through all of the instructions without stopping until the end of the program.
Step Over Button
> The step over button steps through a single instruction in the program and updates all windows for each
> instruction.
Reinitialize Machine Button
> The reinitialize machine button resets the machine's registers and memory contents to default values
Randomize Machine Button
> The randomize machine button sets random values for the machine's registers to simulate how a machine
> might be when the program is introduced in a realistic CPU setting.

# Running the Assembler in Isolation
1. From the root directory navigate to Code
2. Open the Code directory in command line
3. Run command **python runSimulator.py *file/path/to/asm/file.asm* *path/to/output/directory***
4. The output will be written to your second file path argument

# Running the Unit Tests
1. From the root directory navigate to Code
2. Open the Code directory in command line
3. Run command **python runUnitTests.py**

