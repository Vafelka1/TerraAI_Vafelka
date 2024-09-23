import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,\
QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox,\
QLineEdit, QLabel, QStackedWidget, QDialog, QDialogButtonBox

from PyQt6.QtGui import QPalette, QColor


class PushButton(QPushButton):
    def __innit__(self,text,place='Centr'):

        if place=='Centr':
            self.setCentralWidget(QPushButton(text))


class MakeMainPageWin():

    def __innit__(self):
        pass

    def StagesVidgets(self):
    
        HBoxLayout = QHBoxLayout()
    
    
        self.stg_butt_1 = PushButton("1 Stage")
        self.stg_butt_2= PushButton("2 Stage")
        self.stg_butt_3 = PushButton("3 Stage")
        self.stg_butt_4 = PushButton("4 Stage")

        self.stg_butt_1.clicked.connect(SignalsHandler.section_under_development)
        self.stg_butt_2.clicked.connect(SignalsHandler.section_under_development)
        #self.stg_butt_3.clicked.connect(SignalsHandler.stage_3_clicked)
        self.stg_butt_4.clicked.connect(SignalsHandler.section_under_development)
    
        HBoxLayout.addWidget(self.stg_butt_1)
        HBoxLayout.addWidget(self.stg_butt_2)
        HBoxLayout.addWidget(self.stg_butt_3)
        HBoxLayout.addWidget(self.stg_butt_4)
    
        return HBoxLayout
    
    
    def Cell_size(self):
    
        HBoxLayout = QHBoxLayout()
    
        self.sz_butt_1 = PushButton("Cmall Sell")
        self.sz_butt_2 = PushButton("No cmall Sell")
        HBoxLayout.addWidget(self.sz_butt_1)
        HBoxLayout.addWidget(self.sz_butt_2)

        self.sz_butt_1.clicked.connect(SignalsHandler.section_under_development)
    
        return HBoxLayout
    
    
    def Operable_Butt(self):
    
        HBoxLayout = QHBoxLayout()
    
        self.op_butt_1 = PushButton("Operable")
        self.op_butt_2 = PushButton("Unoperable")
        HBoxLayout.addWidget(self.op_butt_1)
        HBoxLayout.addWidget(self.op_butt_2)

        self.op_butt_1.clicked.connect(SignalsHandler.section_under_development)
    
        return HBoxLayout
    
    
    def Therapy_type(self):

        HBoxLayout = QHBoxLayout()
    
        self.th_butt_1 = PushButton("HLT")
        self.th_butt_2 = PushButton("IMMUNO")

        self.th_butt_1.clicked.connect(SignalsHandler.th_butt_1_was_clicked)
        self.th_butt_2.clicked.connect(SignalsHandler.th_butt_2_was_clicked)

        HBoxLayout.addWidget(self.th_butt_1)
        HBoxLayout.addWidget(self.th_butt_2)
    
        return HBoxLayout
    
    
    def Doctor_patient_input(self):
    
        DocHBoxLayout = QHBoxLayout()
        PatientHBoxLayout = QHBoxLayout()
        VBoxLayout = QVBoxLayout()
    
        self.doc_label = QLabel("Doctor:")
        self.patient_label = QLabel("Patient:")
        self.doctor = QLineEdit()
        self.patient = QLineEdit()
    
        DocHBoxLayout.addWidget(self.doc_label)
        DocHBoxLayout.addWidget(self.doctor)
        PatientHBoxLayout.addWidget(self.patient_label)
        PatientHBoxLayout.addWidget(self.patient)
        VBoxLayout.addLayout(DocHBoxLayout)
        VBoxLayout.addLayout(PatientHBoxLayout)
    
        return VBoxLayout
    
    
    def MakeStagesHead(self):
    
        Head_layout = QGridLayout()
    
        stages_layout = self.StagesVidgets()
        size_sell_layout = self.Cell_size()
        operable_layout = self.Operable_Butt()
        therapy_layout = self.Therapy_type()
        doc_patient_inp = self.Doctor_patient_input()
    
    
        Head_layout.addLayout(doc_patient_inp,0,0)
        Head_layout.addLayout(stages_layout,1,0)
        Head_layout.addLayout(size_sell_layout,2,0)
        Head_layout.addLayout(operable_layout,3,0)
        Head_layout.addLayout(therapy_layout,4,0)
    
    
        return Head_layout
    
    def add_race_data(self):
    
        race_combo = QComboBox()
        race_combo.addItems(["Black", "White", "Asian"])
    
        return  race_combo
    
    def add_age_data(self):
    
        age_combo = QComboBox()
        age_combo.addItems(["50", "60", "70"])
    
        return  age_combo
    
    def Data_parsing_page(self):
    
        #QStackedWidget()
    
        # Race
        race_layout = QHBoxLayout()

        self.race_text = QLabel('Choose race:')
        self.race_combo = self.add_race_data()
        self.race_combo.currentTextChanged.connect(SignalsHandler.race_text_changed)

        race_layout.addWidget(self.race_text)
        race_layout.addWidget(self.race_combo)
    
        # Age
        age_layout = QHBoxLayout()

        self.age_text = QLabel('Choose age:')
        self.age_combo = self.add_age_data()
        self.age_combo.currentTextChanged.connect(SignalsHandler.age_text_changed)

        age_layout.addWidget(self.age_text)
        age_layout.addWidget(self.age_combo)
    
        # Combined data
        data_pars_layout = QVBoxLayout()
        data_pars_layout.addLayout(race_layout)
        data_pars_layout.addLayout(age_layout)
    
        return data_pars_layout
    
    def add_doc_ans_combo(self):
    
            cure_layout = QVBoxLayout()
            self.cure_label = QLabel('Cure')
            self.cure = QComboBox()
            self.cure.addItems(["1", "2", "3"])
        
            sure_layout = QVBoxLayout()
            self.sure_label = QLabel('Sure')
            self.sure = QComboBox()
            self.sure.addItems(["1", "2", "3"])
        
            alternative_layout = QVBoxLayout()
            self.alternative_label = QLabel('Alternative')
            self.alternative = QComboBox()
            self.alternative.addItems(["1", "2", "3"])
        
            comment_layout = QVBoxLayout()
            self.comment_label = QLabel('Comment')
            self.comment = QComboBox()
            self.comment.addItems(["1", "2", "3"])
    
            cure_layout.addWidget(self.cure_label)
            cure_layout.addWidget(self.cure)
            sure_layout.addWidget(self.sure_label)
            sure_layout.addWidget(self.sure)
            alternative_layout.addWidget(self.alternative_label)
            alternative_layout.addWidget(self.alternative)
            comment_layout.addWidget(self.comment_label)
            comment_layout.addWidget(self.comment)
    
    
            return  [cure_layout,sure_layout,alternative_layout,comment_layout]
    
    def Doctor_answer(self):
        
            doctor_answer_H_layout = QHBoxLayout()
            doctor_answer_V_layout = QVBoxLayout()
            answer_layout_list = self.add_doc_ans_combo()
    
            for layout in answer_layout_list:
                doctor_answer_H_layout.addLayout(layout)
    
            self.answer_label = QLabel('Choose your method')
            self.setCentralWidget(self.answer_label)
            doctor_answer_V_layout.addWidget(self.answer_label)
            doctor_answer_V_layout.addLayout(doctor_answer_H_layout)
        
    
            return doctor_answer_V_layout

    def Expert_answer(self):

        #expert_text = model.predict()
        expert_text = 'here will bi avr enjoyer answer'
        self.expert_text_label = QLabel(expert_text) 

        return self.expert_text_label

    def Main_page(self):
    
        main_layout = QVBoxLayout()
    
        self.stages_head = self.MakeStagesHead()
        data_parsed = self.Data_parsing_page()
        doctor_answer_comb = self.Doctor_answer()
        expert_answer = self.Expert_answer()
    
        main_layout.addLayout(self.stages_head)
        main_layout.addLayout(data_parsed)
        main_layout.addLayout(doctor_answer_comb)
        main_layout.addWidget(expert_answer)
    
    
        return  main_layout


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Lung Cancer Expert")

        main_page = MakeMainPageWin.Main_page()   
        widget = QWidget()
        widget.setLayout(main_page)
        self.setCentralWidget(widget)    
    

class SignalsHandler():

    def __innit__(self):
        pass

    def th_butt_1_was_clicked(self):
        self.th_butt_1.setText("You already clicked me.")
        self.th_butt_1.setEnabled(False)
    
    def th_butt_2_was_clicked(self):
        self.th_butt_2.setText("You already clicked me.")
        self.th_butt_2.setEnabled(False)

    def section_under_development(self):
        print("section_under_development_clicked")
        dlg = Under_developmaent_Dialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def race_text_changed(self, s):
        print(f'Race: {s}')

    def age_text_changed(self, s): 
        print(f'Age: {s}')


class Under_developmaent_Dialog(QDialog):
    def __init__(self, parent=MainWindow):
        super().__init__(parent)

        self.setWindowTitle("Message")
        under_dev_QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.under_dev_buttonBox = QDialogButtonBox(under_dev_QBtn)
        self.under_dev_buttonBox.accepted.connect(self.accept)
        self.under_dev_buttonBox.rejected.connect(self.reject)

        self.under_dev_layout = QVBoxLayout()
        self.under_dev_message = QLabel("Section under development")
        self.under_dev_layout.addWidget(self.under_dev_message)
        self.under_dev_layout.addWidget(self.under_dev_buttonBox)
        self.setLayout(self.under_dev_layout)


#app = QApplication(sys.argv)
#window = MainWindow()
#window.resize(640, 480)
#window.show()
#app.exec()

if __name__ == __main__:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 480)
    window.show()

    try:
        sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')
