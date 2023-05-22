from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
import sys

class GUI(QMainWindow):
    def __init__(self):
        super(GUI,self).__init__()

    ############### SETTING AND CREATING WINDOW TITLE ##########################

        self.resize(400,400)
        self.setWindowTitle(" calculator ")

    ################### LINE EDIT ##############################################

        self.line_edit=QLineEdit(self)
        self.line_edit.setGeometry(10,10,380,100)

    ################### CLEAR   ###############################################

        self.action_clear=QPushButton(self)
        self.action_clear.setGeometry(10,120,180,60)
        self.action_clear.setText("clear")
        self.action_clear.clicked.connect(self.clear_all)

    ######################  DELEATE ###########################################

        self.action_deleate=QPushButton(self)
        self.action_deleate.setGeometry(200,120,180,60)
        self.action_deleate.setText("delete")
        self.action_deleate.clicked.connect(self.deleate_last)

    ####################### ONE #############################################

        self.action_one=QPushButton(self)
        self.action_one.setGeometry(10,200,85,40)
        self.action_one.setText("1")
        self.action_one.clicked.connect(self.but1)

    #####################   TWO ##################################################

        self.action_two=QPushButton(self)
        self.action_two.setGeometry(101,200,85,40)
        self.action_two.setText("2")
        self.action_two.clicked.connect(self.but2)

    ######################## THREE ##########################################

        self.action_three=QPushButton(self)
        self.action_three.setGeometry(191,200,85,40)
        self.action_three.setText("3")
        self.action_three.clicked.connect(self.but3)

    ########################## PLUS #####################################


        self.action_plus=QPushButton(self)
        self.action_plus.setGeometry(282,200,85,40)
        self.action_plus.setText("+")
        self.action_plus.clicked.connect(self.but4)

    ######################  FOUR  ###########################################


        self.action_four=QPushButton(self)
        self.action_four.setGeometry(10,250,85,40)
        self.action_four.setText("4")
        self.action_four.clicked.connect(self.but5)

    #####################  FIVE ############################################

        self.action_five=QPushButton(self)
        self.action_five.setGeometry(101,250,85,40)
        self.action_five.setText("5")
        self.action_five.clicked.connect(self.but6)

    ####################### SIX #############################################

        self.action_six=QPushButton(self)
        self.action_six.setGeometry(191,250,85,40)
        self.action_six.setText("6")
        self.action_six.clicked.connect(self.but7)

    ####################### MINUS ############################################

        self.action_minus=QPushButton(self)
        self.action_minus.setGeometry(282,250,85,40)
        self.action_minus.setText("-")
        self.action_minus.clicked.connect(self.but8)

    ########################## SEVEN #############################################

        self.action_seven=QPushButton(self)
        self.action_seven.setGeometry(10,300,85,40)
        self.action_seven.setText("7")
        self.action_seven.clicked.connect(self.but9)

    ########################### EIGHT ###########################################

        self.action_eight=QPushButton(self)
        self.action_eight.setGeometry(101,300,85,40)
        self.action_eight.setText("8")
        self.action_eight.clicked.connect(self.but10)

    ###################### NINE ##################################################

        self.action_nine=QPushButton(self)
        self.action_nine.setGeometry(191,300,85,40)
        self.action_nine.setText("9")
        self.action_nine.clicked.connect(self.but11)

    ##################### MULTIPLICATION ########################################

        self.action_astrik=QPushButton(self)
        self.action_astrik.setGeometry(282,300,85,40)
        self.action_astrik.setText("*")
        self.action_astrik.clicked.connect(self.but12)

    ###################### ZERO #######################################################

        self.action_zero=QPushButton(self)
        self.action_zero.setGeometry(10,350,85,40)
        self.action_zero.setText("0")
        self.action_zero.clicked.connect(self.but13)

    ##################### POINT ######################################################

        self.action_point=QPushButton(self)
        self.action_point.setGeometry(101,350,85,40)
        self.action_point.setText(".")
        self.action_point.clicked.connect(self.but14)

    ################### DIVISON ##########################################################

        self.action_divison=QPushButton(self)
        self.action_divison.setGeometry(191,350,85,40)
        self.action_divison.setText("/")
        self.action_divison.clicked.connect(self.but15)

    ################### EQUALL #############################################################

        self.action_equall=QPushButton(self)
        self.action_equall.setGeometry(282,350,85,40)
        self.action_equall.setText("=")
        self.action_equall.clicked.connect(self.result)


    def clear_all(self):
        self.line_edit.setText(" ")

    def deleate_last(self):
        text=self.line_edit.text()
        self.line_edit.setText(text[:len(text)-1])

    ################### ONE ###############################################################

    def but1(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "1")

    ################### TWO ################################################################

    def but2(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "2")

    ######################## THREE ####################################################

    def but3(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "3")

    ######################### PLUS ###################################################

    def but4(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "+")

    ########################  FOUR   ###############################################

    def but5(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "4")
    #########################  FIVE  ###############################################

    def but6(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "5")

    #########################   SIX  ##################################################

    def but7(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "6")

    ######################### MINUS ###############################################

    def but8(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "-")

    ######################### SEVEN ###############################################

    def but9(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ " 7")

    ######################### EIGHT ##############################################

    def but10(self):
        A = self.line_edit.text()
        self.line_edit.setText(A+ "8")

    ######################### NINE ###################################################

    def but11(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "9")

    ################### MULTIPLICATION ####################################################

    def but12(self):
        A=self.line_edit.Text()
        self.line_edit.setText(A+ " *")

    #####################   ZERO #################################################################

    def but13(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "0")

    ####################  POINT(.) #####################################################################

    def but14(self):
        A=self.line_edit.text()
        self.line_edit.setTex(A+ ".")

    ##################### DIVISON #################################################################

    def but15(self):
        A=self.line_edit.text()
        self.line_edit.setText(A+ "/")

    ######################  RESULT #################################################################

    def result(self):
        equ=self.line_edit.text()
        ans=eval(equ)
        self.line_edit.setText(str(ans))

    ###############################################################################################
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=GUI()
    w.show()
    sys.exit(app.exec_())

