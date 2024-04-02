import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTextEdit
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5 import uic
from asyncqt import QEventLoop, asyncSlot
from ..Assembler import LC3_Assembler
from ..Sim import LC3_Simulator
from ..Supporting_Libraries import utils

LINE_TIMER_TIME = 50

class AssembleXperience(QWidget):
    
    scroll_signal = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        
        path = os.path.dirname(os.path.abspath(__file__))
        # Load the UI file
        uic.loadUi(path + "\\simulator.ui", self)
        
        self.init_timers()
        self.init_signals()
        self.init_widget_settings()
        self.init_variables()
        self.init_actions()
        
        self.change_state()
             
        # Show the widget
        self.show()
        
    def init_widget_settings(self) -> None:
        # Sets text editor to side-scroll instead of wrapping text.
        self.Edit_EditorTextEditor.setLineWrapMode(QTextEdit.NoWrap)
        self.Edit_LineNumberTextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    def init_signals(self) -> None:
        self.scroll_signal.connect(self.scroll_to_program_counter)
        
    def init_actions(self) -> None:
        self.populate_line_numbers()
        
        self.Application_TabWidget.currentChanged.connect(self.change_state)
        
        self.Edit_NewButton.clicked.connect(self.clear_editor)
        self.Edit_SaveButton.clicked.connect(self.save_editor)
        self.Edit_LoadButton.clicked.connect(self.load_editor)
        self.Edit_AssembleButton.clicked.connect(self.assemble_editor)
        
        self.Simulate_LoadButton.clicked.connect(self.load_simulator)
        self.Simulate_StepButton.clicked.connect(self.step_over)
        
    def init_timers(self) -> None:
        self.editor_line_timer = QTimer()
        self.editor_line_timer.timeout.connect(self.populate_line_numbers)
        
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
        
        self.currentState = 'simulate'
        self.editor_loaded_file = ''
        
        self.simulator_loaded_file = ''
        self.machine_state = None
        
        self.font_height = self.Simulate_SimulatorTextBrowser.fontMetrics().height()
        
    def change_state(self) -> None:
        current_index = str(self.Application_TabWidget.currentIndex())
        self.states[current_index]()
        
    def state_simulate(self) -> None:
        self.editor_line_timer.stop()
    
    def state_edit(self) -> None:
        self.editor_line_timer.start(LINE_TIMER_TIME)
            
    def populate_line_numbers(self) -> None:
        self.Edit_LineNumberTextBrowser.clear()
        editor_contents = self.get_editor_text()
        line_number = editor_contents.count("\n") + 1
        for i in range(0, line_number):
            self.Edit_LineNumberTextBrowser.append(f"{i+1}.")
            
    def populate_editor_file_name_display(self) -> None:
        self.Edit_FileNameTextBrowser.clear()
        self.Edit_FileNameTextBrowser.append(f"Editing: {os.path.split(self.editor_loaded_file)[-1]}")
        
    def write_to_editor(self, string: str) -> None:
        self.Edit_EditorTextEditor.clear()
        self.Edit_EditorTextEditor.append(string)
        
    def write_to_editor_console(self, string: str) -> None:
        self.Edit_ConsoleTextBrowser.clear()
        self.Edit_ConsoleTextBrowser.append(string)
            
    def clear_editor(self) -> None:
        self.Edit_EditorTextEditor.clear()
        self.editor_loaded_file = ''
        self.populate_editor_file_name_display()
        
    def get_editor_text(self) -> str:
        return self.Edit_EditorTextEditor.toPlainText()
        
    def save_editor(self) -> None:
        if self.editor_loaded_file and os.path.exists(self.editor_loaded_file):
            os.remove(self.editor_loaded_file)
            content = self.get_editor_text()
            utils.write_to_file(content, self.editor_loaded_file)
        else:
            self.save_as_editor()

    def save_as_editor(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Asm Files (*.asm);;Bin Files (*.bin);;All Files(*) ", options=options)
        content = self.get_editor_text()
        utils.write_to_file(content, file_path)
        
    def load_editor(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)
        content = utils.read_from_file(file_path)
        if content:
            self.write_to_editor(content)
            self.editor_loaded_file = file_path
            self.populate_editor_file_name_display()
        
    def assemble_editor(self) -> None:
        if self.editor_loaded_file:
            assembler_return_string = LC3_Assembler.assemble(self.editor_loaded_file)
            
        else:
            split_path = os.path.split(self.editor_loaded_file)
            directory, asm_file_name_no_extension = split_path[0], split_path[1].split('.')[0]
            bin_file_name = f"{asm_file_name_no_extension}.bin"
            bin_file_path = f"{directory}\\{bin_file_name}"
           
            if utils.write_to_file(assembler_return_string, bin_file_path):
                self.write_to_editor_console(f"{bin_file_path} assembled successfully!")
            else:
                self.write_to_editor_console(f"Error: assembly unsuccessful, could not write to {bin_file_path}.")
                
    def populate_simulator_file_name_display(self) -> None:
        self.Simulate_FileNameTextBrowser.clear()
        self.Simulate_FileNameTextBrowser.append(f"Simulating: {os.path.split(self.simulator_loaded_file)[-1]}")
                
    def load_simulator(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "OBJ2 Files (*.obj2)", options=options)
        content = utils.read_from_file(file_path)
        if content:
            self.generate_simulation(file_path)
            self.simulator_loaded_file = file_path
            self.populate_simulator_file_name_display()
            
    def generate_simulation(self, obj2_file_path: str) -> None:
        self.machine_state = LC3_Simulator.create_simulation(obj2_file_path)
        self.refresh_simulation()
        
    def refresh_simulation(self) -> None:
        self.write_memory_space_to_simulator_window()
        self.write_registers_to_register_window()
        self.write_output_to_console()
        
    def write_memory_space_to_simulator_window(self) -> None:
        self.Simulate_SimulatorTextBrowser.clear()
        memory_space_string = ""
        program_counter_string = utils.int_to_hex(self.machine_state.registers['PC'])
        counter = 0
        for address, content in self.machine_state.memory_space.items():
            
            if content and address == program_counter_string:
                memory_space_string += f'| -> {address}\t\t{content[0]}\t{content[1]}\n'
                arrow_line_num = counter
            elif address == program_counter_string:
                memory_space_string += f'| -> {address}\n'
                arrow_line_num = counter
            elif content:
                memory_space_string += f"|    {address}\t\t{content[0]}\t{content[1]}\n"
            else:
                memory_space_string += f"|    {address}\n"
            counter += 1

        self.Simulate_SimulatorTextBrowser.append(memory_space_string)
        QTimer.singleShot(750, lambda: self.scroll_signal.emit(arrow_line_num))
        
    def scroll_to_program_counter(self, line_num) -> None:
        # cursor = QTextCursor(self.Simulate_SimulatorTextBrowser.document().findBlockByLineNumber(line_num + 45))
        # self.Simulate_SimulatorTextBrowser.setTextCursor(cursor)
        # self.Simulate_SimulatorTextBrowser.ensureCursorVisible()
        position = self.font_height * (line_num)
        self.Simulate_SimulatorTextBrowser.verticalScrollBar().setValue(position)
    
    def write_registers_to_register_window(self) -> None:
        self.Simulate_RegistersTextBrowser.clear()
        register_string = ""
        for register, value in self.machine_state.registers.items():
            if register != "CC":
                register_string += f"{register}\t{utils.int_to_hex(value)}\n\n"
            else:
                register_string += f"{register}\t{value}"
        self.Simulate_RegistersTextBrowser.append(register_string)
        self.Simulate_RegistersTextBrowser.verticalScrollBar().setValue(0)
    
    def write_output_to_console(self) -> None:
        self.Simulate_ConsoleTextEditor.clear()
        self.Simulate_ConsoleTextEditor.append(self.machine_state.console_output)
        
    def step_over(self) -> None:
        self.machine_state = LC3_Simulator.step_over(self.machine_state)
        self.refresh_simulation()
                
def main(): 
    app = QApplication(sys.argv)
    widget = AssembleXperience()
    sys.exit(app.exec_())