import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTextEdit
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import uic
from asyncqt import QEventLoop, asyncSlot
from ..Assembler import LC3_Assembler
from ..Supporting_Libraries import utils

LINE_TIMER_TIME = 50

class AssembleXperience(QWidget):
    def __init__(self):
        super().__init__()
        
        path = os.path.dirname(os.path.abspath(__file__))
        # Load the UI file
        uic.loadUi(path + "\\simulator.ui", self)
        
        self.init_timers()
        self.init_widget_settings()
        self.init_variables()
        self.init_actions()
        
        self.change_state()
             
        # Show the widget
        self.show()
        
    def init_widget_settings(self) -> None:
        # Sets text editor to side-scroll instead of wrapping text.
        self.Edit_EditorTextEditor.setLineWrapMode(QTextEdit.NoWrap)
        
    def init_actions(self) -> None:
        self.populate_registers()
        self.populate_line_numbers()
        
        self.Application_TabWidget.currentChanged.connect(self.change_state)
        
        self.Edit_NewButton.clicked.connect(self.clear_editor)
        self.Edit_SaveButton.clicked.connect(self.save_editor)
        self.Edit_LoadButton.clicked.connect(self.load_editor)
        self.Edit_AssembleButton.clicked.connect(self.assemble_editor)
        
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
        
    def change_state(self) -> None:
        current_index = str(self.Application_TabWidget.currentIndex())
        self.states[current_index]()
        
    def state_simulate(self) -> None:
        self.editor_line_timer.stop()
    
    def state_edit(self) -> None:
        self.editor_line_timer.start(LINE_TIMER_TIME)
        
    def populate_registers(self) -> None:
        self.Simulate_RegistersTextBrowser.clear()
        for reg_name, reg_val in self.registers_dict.items():
            self.Simulate_RegistersTextBrowser.append(f"{reg_name}:  {reg_val}\n")
            
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
        
    def assemble_editor(self) -> str:
        if self.editor_loaded_file:
            assembler_return_string, error = LC3_Assembler.assemble(self.editor_loaded_file)
            
        if error:
            self.write_to_editor_console(assembler_return_string)
            
        else:
            split_path = os.path.split(self.editor_loaded_file)
            directory, asm_file_name_no_extension = split_path[0], split_path[1].split('.')[0]
            bin_file_name = f"{asm_file_name_no_extension}.bin"
            bin_file_path = f"{directory}\\{bin_file_name}"
           
            if utils.write_to_file(assembler_return_string, bin_file_path):
                self.write_to_editor_console(f"{bin_file_path} assembled successfully!")
            else:
                self.write_to_editor_console(f"Error: assembly unsuccessful, could not write to {bin_file_path}.")
                
def main(): 
    app = QApplication(sys.argv)
    widget = AssembleXperience()
    sys.exit(app.exec_())

main()