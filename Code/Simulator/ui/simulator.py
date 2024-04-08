import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTextEdit, QTextBrowser
from PyQt5.QtCore import QTimer, Qt, QEvent
from PyQt5.QtGui import QTextOption
from PyQt5 import uic
from asyncqt import QEventLoop, asyncSlot
from ..Assembler import LC3_Assembler
from ..Sim import LC3_Simulator
from ..Supporting_Libraries import utils

class AssembleXperience(QWidget):
    
    def __init__(self):
        super().__init__()
        
        path = os.path.dirname(os.path.abspath(__file__))
        # Load the UI file
        uic.loadUi(path + "\\simulator.ui", self)
        self.setWindowTitle("AssembleXperience")
        
        self.init_timers()
        self.init_widget_settings()
        self.init_variables()
        self.init_actions()
        
        self.change_state()
             
        # Show the widget
        self.show()
        
    def init_widget_settings(self) -> None:
        # Sets text editor and simulator to side-scroll instead of wrapping text.
        self.Edit_EditorTextEditor.setLineWrapMode(QTextEdit.NoWrap)
        self.Simulate_SimulatorTextBrowser.setLineWrapMode(QTextBrowser.NoWrap)
        
        # Hide vertical scroll bar for the line number text editor
        self.Edit_LineNumberTextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Hide horizontal scroll bar for the simulator text
        self.Simulate_SimulatorTextBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Set the input line edit to only take one character at a time
        self.Simulate_ConsoleLineEdit.setMaxLength(1)

        # Install event filter for widgets that need it.
        self.Simulate_SimulatorTextBrowser.installEventFilter(self)
        self.Simulate_JumpToLineEdit.installEventFilter(self)
        self.Edit_EditorTextEditor.installEventFilter(self)
        
    def init_actions(self) -> None:
        self.populate_line_numbers()
        
        self.Application_TabWidget.currentChanged.connect(self.change_state)
        
        self.Edit_NewButton.clicked.connect(self.clear_editor)
        self.Edit_SaveButton.clicked.connect(self.save_editor)
        self.Edit_LoadButton.clicked.connect(self.load_editor)
        self.Edit_AssembleButton.clicked.connect(self.assemble_editor)
        
        self.Simulate_LoadButton.clicked.connect(self.load_simulator)
        self.Simulate_ReloadButton.clicked.connect(self.reload_simulator)
        self.Simulate_StepButton.clicked.connect(self.step_over)
        self.Simulate_RunButton.clicked.connect(self.run)
        self.Simulate_RandomizeButton.clicked.connect(self.randomize_machine)
        
        
        self.breakpoint1.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint2.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint3.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint4.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint5.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint6.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint7.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint8.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint9.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint10.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint11.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint12.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint13.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint14.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint15.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint16.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint17.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint18.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint19.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint20.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint21.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint22.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint23.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint24.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint25.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint26.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint27.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint28.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint29.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint30.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint31.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint32.stateChanged.connect(self.breakpoint_activated)
        self.breakpoint33.stateChanged.connect(self.breakpoint_activated)
        
    def init_timers(self) -> None:
        self.editor_line_timer = QTimer()
        self.editor_line_timer.timeout.connect(self.populate_line_numbers)
        
        self.check_for_input_timer = QTimer()
        self.check_for_input_timer.timeout.connect(self.check_for_input)
        
        self.resume_timer = QTimer()
        self.resume_timer.timeout.connect(self.resume_running)
        
    def init_variables(self) -> None:
        self.registers_dict = {
            'R0' : '0',
            'R1' : '0',
            'R2' : '0',
            'R3' : '0',
            'R4' : '0',
            'R5' : '0',
            'R6' : '0',
            'R7' : '0',
            'PC' : '0',
            'MSR': '0'
        }
        
        self.states = {
            '0': self.state_simulate,
            '1': self.state_edit
        }
        
        self.line_timer_time = 50
        self.check_for_input_time = 10
        self.resume_timer_time = 50
        
        self.currentState = 'simulate'
        self.editor_loaded_file = ''
        
        self.simulator_loaded_file = ''
        self.machine_state = None
        
        self.save_needed = False
        
        self.font_height = self.Simulate_SimulatorTextBrowser.fontMetrics().height()
        
        self.disable_buttons_during_input = [
            self.Simulate_RunButton,
            self.Simulate_StepButton,
            self.Simulate_RandomizeButton
        ]
        
        self.mem_counter = 0
        self.lines_on_screen = 34
        
        self.breakpoints = [
            self.breakpoint1,
            self.breakpoint2,
            self.breakpoint3,
            self.breakpoint4,
            self.breakpoint5,
            self.breakpoint6,
            self.breakpoint7,
            self.breakpoint8,
            self.breakpoint9,
            self.breakpoint10,
            self.breakpoint11,
            self.breakpoint12,
            self.breakpoint13,
            self.breakpoint14,
            self.breakpoint15,
            self.breakpoint16,
            self.breakpoint17,
            self.breakpoint18,
            self.breakpoint19,
            self.breakpoint20,
            self.breakpoint21,
            self.breakpoint22,
            self.breakpoint23,
            self.breakpoint24,
            self.breakpoint25,
            self.breakpoint26,
            self.breakpoint27,
            self.breakpoint28,
            self.breakpoint29,
            self.breakpoint30,
            self.breakpoint31,
            self.breakpoint32,
            self.breakpoint33
        ]
        
    def eventFilter(self, obj: object, event) -> object:
        # Event filter to scroll through simulation address space
        if obj == self.Simulate_SimulatorTextBrowser and event.type() == event.Wheel:
            if self.machine_state:
                delta = event.angleDelta().y()
                # Stop from scrolling past min limit
                if delta > 0 and self.mem_counter > 0:
                    self.mem_counter -= 1
                # Stop from scrolling past max limit
                elif self.mem_counter < utils.FOUR_DIG_HEX_MAX - self.lines_on_screen:
                    self.mem_counter += 1
            
                self.write_memory_space_to_simulator_window()
            
        if obj == self.Edit_EditorTextEditor and event.type() == QEvent.KeyPress:
            if self.editor_loaded_file and not self.save_needed:
                self.save_needed = True
                self.populate_editor_file_name_display()
        
        # Even filter to search for addresses in address space using Jump To
        if obj == self.Simulate_JumpToLineEdit and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.search_for_address()
            
        return super().eventFilter(obj, event)
    
    # Changes certain properties depending on what tab you're on.
    def change_state(self) -> None:
        current_index = str(self.Application_TabWidget.currentIndex())
        self.states[current_index]()
    
    # Changes properties to what is necessary for simulate tab
    def state_simulate(self) -> None:
        self.Simulate_ConsoleLineEdit.clear()
        self.Simulate_ConsoleLineEdit.setReadOnly(True)
        for button in self.disable_buttons_during_input:
            button.setEnabled(True)
        self.editor_line_timer.stop()
        self.check_for_input_timer.stop()
    
    # Changes properties to what is necessary for edit tab
    def state_edit(self) -> None:
        self.editor_line_timer.start(self.line_timer_time)
    
    # Changes some properties for commands like GETC and IN so char input can be taken
    # without program advancement.
    def get_input(self) -> None:
        self.Simulate_ConsoleLineEdit.setReadOnly(False)
        self.check_for_input_timer.start(self.check_for_input_time)
        for button in self.disable_buttons_during_input:
            button.setEnabled(False)
    
    # Adds the line numbers to the editor depending on how many lines are in it.
    def populate_line_numbers(self) -> None:
        self.Edit_LineNumberTextBrowser.clear()
        editor_contents = self.get_editor_text()
        line_number = editor_contents.count("\n") + 1
        for i in range(0, line_number):
            self.Edit_LineNumberTextBrowser.append(f"{i+1}.")
    
    # Shows loaded file in editor
    def populate_editor_file_name_display(self) -> None:
        save_needed_string = ''
        if self.save_needed:
            save_needed_string = '*'
            self.save_needed = False
        self.Edit_FileNameTextBrowser.clear()
        self.Edit_FileNameTextBrowser.append(f"Editing: {os.path.split(self.editor_loaded_file)[-1]} {save_needed_string}")
    
    # Writes string contents to editor
    def write_to_editor(self, string: str) -> None:
        self.Edit_EditorTextEditor.clear()
        self.Edit_EditorTextEditor.append(string)
    
    # Writes string contents to editor console
    def write_to_editor_console(self, string: str) -> None:
        self.Edit_ConsoleTextBrowser.clear()
        self.Edit_ConsoleTextBrowser.append(string)
    
    # Clears the editor
    def clear_editor(self) -> None:
        self.Edit_EditorTextEditor.clear()
        self.editor_loaded_file = ''
        self.populate_editor_file_name_display()
    
    # Gets the editor string contents
    def get_editor_text(self) -> str:
        return self.Edit_EditorTextEditor.toPlainText()
    
    # Saves the contents of the editor to a file
    def save_editor(self) -> None:
        # If the file has already been created save to it
        if self.editor_loaded_file and os.path.exists(self.editor_loaded_file):
            os.remove(self.editor_loaded_file)
            content = self.get_editor_text()
            utils.write_to_file(content, self.editor_loaded_file)
        # If the file is new then show file save dialogue
        else:
            self.save_as_editor()
            self.populate_editor_file_name_display()
        self.save_needed = False
        self.populate_editor_file_name_display()

    # Show file save dialogue for editor
    def save_as_editor(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Asm Files (*.asm);;Bin Files (*.bin);;All Files(*) ", options=options)
        content = self.get_editor_text()
        utils.write_to_file(content, file_path)
        self.editor_loaded_file = file_path
    
    # Load a file into the editor
    def load_editor(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)
        content = utils.read_from_file(file_path)
        if content:
            self.write_to_editor(content)
            self.editor_loaded_file = file_path
            self.populate_editor_file_name_display()
    
    # Assemble the file that was loaded into the editor (not the contents of the editor)
    def assemble_editor(self) -> None:
        self.Edit_ConsoleTextBrowser.clear()
        if self.editor_loaded_file:
            assembler_return_string = LC3_Assembler.assemble(self.editor_loaded_file)
            split_path = os.path.split(self.editor_loaded_file)
            directory, asm_file_name_no_extension = split_path[0], split_path[1].split('.')[0]
            self.Edit_ConsoleTextBrowser.append(assembler_return_string)
    
    # Show the file that was loaded into the simulator
    def populate_simulator_file_name_display(self) -> None:
        self.Simulate_FileNameTextBrowser.clear()
        self.Simulate_FileNameTextBrowser.append(f"Simulating: {os.path.split(self.simulator_loaded_file)[-1]}")
                
    # Load a file into the simulator
    def load_simulator(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "OBJ2 Files (*.obj2)", options=options)
        content = utils.read_from_file(file_path)
        if content:
            self.generate_simulation(file_path)
            self.simulator_loaded_file = file_path
            self.populate_simulator_file_name_display()
    
    # Create the simulation based on the obj2 file that was chosen to load
    def generate_simulation(self, obj2_file_path: str, random=False) -> None:
        self.Simulate_ConsoleTextBrowser.clear()
        self.Simulate_RunButton.setEnabled(True)
        self.Simulate_StepButton.setEnabled(True)        
        self.machine_state = LC3_Simulator.create_simulation(obj2_file_path, random)
        self.mem_counter = self.machine_state.registers["PC"]
        self.refresh_simulation()
    
    # Stop the simulation
    def halt_simulation(self) -> None:
        self.Simulate_RunButton.setEnabled(False)
        self.Simulate_StepButton.setEnabled(False)
    
    # Restart the simulation using the obj2 file that was previously loaded 
    def reload_simulator(self) -> None:
        self.generate_simulation(self.simulator_loaded_file)
        
    # Clear all registers and addresses.
    def reinitialize_machine(self):
        self.machine_state.memory_space = self.machine_state.init_memory_space(random=False)
        self.machine_state.registers = self.machine_state.init_state(random=False)
        self.machine_state.write_instructions_to_memory_space()
        self.refresh_simulation()
    
    # Randomize all registers and addresses.
    def randomize_machine(self):
        if self.simulator_loaded_file:
            self.generate_simulation(self.simulator_loaded_file, random=True)
    
    # Rewrite all contents to the simulator windows
    def refresh_simulation(self) -> None:
        if self.machine_state.running:
            
            if self.machine_state.input_mode:
                self.get_input()
            
            else:    
                self.write_memory_space_to_simulator_window()
                self.write_registers_to_register_window()
                self.write_output_to_console()
        else:
            self.halt_simulation()
    
    # Check to see if the user has inputted a character
    def check_for_input(self):
        input_mode = self.machine_state.input_mode
        input = self.Simulate_ConsoleLineEdit.text()
        if len(input) > 0:
            if input_mode == 1:
                self.machine_state.console_output = input
            self.machine_state.registers['R0'] = ord(input)
            self.machine_state.input_mode = 0
            self.machine_state.registers['PC'] += 1
            self.state_simulate()
            
        self.refresh_simulation()
    
    # Write the currently selected for display contents of the memory space to the simulator window
    def write_memory_space_to_simulator_window(self) -> None:        
        self.Simulate_SimulatorTextBrowser.clear()
        memory_space_string = ""
        program_counter = self.machine_state.registers['PC']
        mem_count = self.mem_counter
        mem_count_end = mem_count + self.lines_on_screen - 1
        address_space = list(self.machine_state.memory_space.keys())
        
        # If there is an address searched for that would exceed the bounds of the memory_space,
        # then only display the last 34 addresses.
        if not utils.int_to_hex(mem_count_end) in address_space:
            mem_count = utils.hex_to_int(address_space[-1]) - self.lines_on_screen
            mem_count_end = mem_count + self.lines_on_screen - 1
            
        address_list = list(range(mem_count, mem_count_end))
        breakpoint_status_list = []
        
        # Write the contents
        for addr in address_list:
            addr_str = utils.int_to_hex(addr)
            contents = self.machine_state.memory_space[addr_str]
            breakpoint_status_list.append(True) if 'b' in contents else breakpoint_status_list.append(False)
            memory_space_string += f"|    {addr_str}\t" if addr != program_counter else f"| -> {addr_str}\t"
            for content in contents:
                if content != 'x' and content != 'b':
                    memory_space_string += f"{content}\t"
            memory_space_string += '\n'
        self.Simulate_SimulatorTextBrowser.append(memory_space_string.removesuffix('\n'))
        
        # Set the breakpoints
        for bp_status, breakpoint in zip(breakpoint_status_list, self.breakpoints):
            breakpoint.setChecked(bp_status)
            
    # Searches memory space for the address that's entered into Jump To and then goes to it if found
    def search_for_address(self) -> None:
        address = self.Simulate_JumpToLineEdit.text()
        if self.machine_state and utils.is_hex(address):
            mem_space_addresses = self.machine_state.memory_space.keys()
            if address in mem_space_addresses:
                self.mem_counter = utils.hex_to_int(address)
                self.write_memory_space_to_simulator_window()
    
    # Writes the contents of the machine's registers to the register window
    def write_registers_to_register_window(self) -> None:
        self.Simulate_RegistersTextBrowser.clear()
        register_string = ""
        for register, value in self.machine_state.registers.items():
            if register != "CC":
                register_string += f"{register}\t{utils.int_to_hex(value)}\t{value}\n\n"
            else:
                register_string += f"{register}\t{value}"
        self.Simulate_RegistersTextBrowser.append(register_string)
        self.Simulate_RegistersTextBrowser.verticalScrollBar().setValue(0)
    
    # If the machine has content then writes it and clears the content
    def write_output_to_console(self) -> None:
        self.Simulate_ConsoleTextBrowser.append(self.machine_state.console_output)
        self.machine_state.console_output = ""
    
    # Step over one instruction
    def step_over(self) -> None:
        self.machine_state = LC3_Simulator.step_over(self.machine_state)
        self.refresh_simulation()
    
    # Resume running if character input has been collected
    def resume_running(self):
        if not self.machine_state.input_mode:
            self.resume_timer.stop()
            self.run()
    
    # Run through the whole program, pausing if in input mode. If input mode the launch a timer
    # to check for user input.
    def run(self) -> None:
        self.machine_state.paused = False
        while self.machine_state.running and not self.machine_state.input_mode and not self.machine_state.paused:
            self.machine_state = LC3_Simulator.step_over(self.machine_state)
            program_counter = utils.int_to_hex(self.machine_state.registers['PC'])
            current_instruction = self.machine_state.memory_space[program_counter]
            if 'b' in current_instruction:
                self.machine_state.paused = True
            if not self.machine_state.input_mode:
                self.refresh_simulation()
            if '0'*16 in current_instruction:
                self.machine_state.running = False
        
        if self.machine_state.paused:
            self.refresh_simulation()
            
        if self.machine_state.input_mode:
            self.refresh_simulation()
            self.resume_timer.start(self.resume_timer_time)
    
    # Runs if a breakpoint is checked, appends 'b' to content to signify that it should have a breakpoint attached.
    def breakpoint_activated(self):
        if self.simulator_loaded_file and self.machine_state.running:
            mem_count = self.mem_counter
            mem_count_end = mem_count + self.lines_on_screen - 1
            
            address_list = list(range(mem_count, mem_count_end))
            
            for addr, breakpoint in zip(address_list, self.breakpoints):
                addr_str = utils.int_to_hex(addr)
                contents = self.machine_state.memory_space[addr_str]
                if breakpoint.isChecked():
                    if not 'b' in contents:
                        contents.append('b')
                else:
                    if 'b' in contents:
                        contents.remove('b')
            
                
                
def main(): 
    app = QApplication(sys.argv)
    widget = AssembleXperience()
    sys.exit(app.exec_())