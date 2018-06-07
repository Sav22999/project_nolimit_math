## NOLIMIT SVILUPPATO DA SAVERIO MORELLI - LICENZA GNU V3
## VERSIONE SCRIPT V1.0
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_noLimit(object):
    def setupUi(self, noLimit):
        noLimit.setObjectName("noLimit")
        noLimit.resize(800, 354)
        noLimit.setMinimumSize(QtCore.QSize(800, 354))
        noLimit.setMaximumSize(QtCore.QSize(800, 354))
        noLimit.setGeometry(30, 30, 800, 354)
        font = QtGui.QFont()
        font.setPointSize(18)
        noLimit.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        noLimit.setWindowIcon(icon)
        noLimit.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(noLimit)
        self.centralwidget.setObjectName("centralwidget")
        self.bttCalcola = QtWidgets.QPushButton(self.centralwidget)
        self.bttCalcola.setGeometry(QtCore.QRect(320, 280, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bttCalcola.setFont(font)
        self.bttCalcola.setObjectName("bttCalcola")
        self.textX = QtWidgets.QLineEdit(self.centralwidget)
        self.textX.setGeometry(QtCore.QRect(50, 210, 31, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textX.setFont(font)
        self.textX.setText("")
        self.textX.setObjectName("textX")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 58, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 58, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textNumeratore = QtWidgets.QLineEdit(self.centralwidget)
        self.textNumeratore.setGeometry(QtCore.QRect(90, 140, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textNumeratore.setFont(font)
        self.textNumeratore.setObjectName("textNumeratore")
        self.textDenominatore = QtWidgets.QLineEdit(self.centralwidget)
        self.textDenominatore.setGeometry(QtCore.QRect(90, 190, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textDenominatore.setFont(font)
        self.textDenominatore.setObjectName("textDenominatore")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 170, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(403, -20, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textRisultato = QtWidgets.QLineEdit(self.centralwidget)
        self.textRisultato.setGeometry(QtCore.QRect(560, 10, 231, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textRisultato.setFont(font)
        self.textRisultato.setReadOnly(True)
        self.textRisultato.setObjectName("textRisultato")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 391, 91))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 20, 271, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.textX.raise_()
        self.textDenominatore.raise_()
        self.textNumeratore.raise_()
        self.textRisultato.raise_()
        self.bttCalcola.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        noLimit.setCentralWidget(self.centralwidget)

        self.retranslateUi(noLimit)
        QtCore.QMetaObject.connectSlotsByName(noLimit)

    def retranslateUi(self, noLimit):
        _translate = QtCore.QCoreApplication.translate
        noLimit.setWindowTitle(_translate("noLimit", "NoLimit v.1 - by Saverio Morelli"))
        self.bttCalcola.setText(_translate("noLimit", "Calcola e\n"
"genera il grafico"))
        self.label.setText(_translate("noLimit", "lim"))
        self.label_2.setText(_translate("noLimit", "x →"))
        self.label_4.setText(_translate("noLimit", "<html><head/><body><p><img src=\"./icona.png\"/><span style=\" font-style:italic; color:#ff0000; vertical-align:super;\">Realizzato da Saverio Morelli</span></p></body></html>"))
        self.label_5.setText(_translate("noLimit", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; color:#ff0000;\">NoLimit Math</span></p></body></html>"))
        self.label_6.setText(_translate("noLimit", "Risultato:"))
        
        self.textDenominatore.setText("1")
        self.bttCalcola.clicked.connect(self.onClickCalcola)
        
    def onClickCalcola(self):
        numeratore=1
        denominatore=1
        x0=0
        risultato=1
        if(self.textNumeratore.text()!=""):
            print("Numeratore: OK")
            print(len(self.textNumeratore.text()))
            array=list(self.textNumeratore.text())
            print(array)
# =============================================================================
#             inizio calcolo di "a"
# =============================================================================
            a=0
            if("x^2" in self.textNumeratore.text()):
                print("Esiste ax^2")
                volta=0
                negativo=False
                if(array[0]=="-"):
                    negativo=True
                    del array[0]
                while(array[0]!="x"):
                    if(volta!=0):
                        a*=10;
                    volta+=1
                    a+=int(array[0]);
                    del array[0]
                if(a==0):
                    a=1
                if(negativo):
                    a*=-1;
                print("a = " + str(a))
                del array[0]
                del array[0]
                del array[0]
            print(array)
# =============================================================================
#             identificazione operazione da "a"
# =============================================================================
            operazionedaa='+'
            if(len(array)>=2 and (array[0]=="+" or array[0]=="-")):
                operazionedaa=array[0]
                del array[0]
# =============================================================================
#             inizio calcolo di b
# =============================================================================
            operazionedab=operazionedaa
            b=0
            if("x" in array):
                print("Esiste bx")
                volta=0
                negativo=False
                if(len(array)>=4 and array[0]=="(" and array[1]=="-"):
                    negativo=True
                    del array[0]
                    del array[0]
                while(array[0]!="x"):
                    if(volta!=0):
                        b*=10;
                    volta+=1
                    b+=int(array[0]);
                    del array[0]
                if(b==0):
                    b=1
                if(negativo):
                    b*=-1
                print("b = " + str(b))
                del array[0]
                if(array[0]==")"):
                    del array[0]
                
                if(len(array)>=2 and (array[0]=="+" or array[0]=="-")):
                    operazionedab=array[0]
                    del array[0]
# =============================================================================
#             inizio calcolo di c
# =============================================================================
            print(array)
            c=0
            if(len(array)>=1):
                print("Esiste c")
                volta=0
                negativo=False
                if(len(array)>=4 and array[0]=="(" and array[1]=="-"):
                    negativo=True
                    del array[0]
                    del array[0]
                    del array[len(array)-1]
                    print(array)
                print(array)
                while(len(array)>0):
                    if(not volta==0):
                        c*=10;
                    volta+=1
                    c+=int(array[0]);
                    del array[0]
                if(negativo):
                    c*=-1;
                print("c = " + str(c))
            print(str(a) + "x^2" + str(operazionedaa) + str(b) + "x" + str(operazionedab) + str(c))
# =============================================================================
#             operazione1=0
#             if(operazionedaa)
# =============================================================================
        else:
            print("Numeratore: Error | Empty")
        
        if(self.textDenominatore.text()!="" or self.textDenominatore.text()!="0"):
            if(self.textDenominatore.text()=="1"):
                print("Denominatore: OK | Static (1)")
            else:
                print("Denominatore: OK | Custom")
                print(len(self.textDenominatore.text()))
                array=list(self.textDenominatore.text())
                print(array)
# =============================================================================
#            inizio calcolo di "a"
# =============================================================================
                a=0
                if("x^2" in self.textDenominatore.text()):
                    print("Esiste ax^2")
                    volta=0
                    negativo=False
                    if(array[0]=="-"):
                        negativo=True
                        del array[0]
                    while(array[0]!="x"):
                        if(volta!=0):
                            a*=10;
                        volta+=1
                        a+=int(array[0]);
                        del array[0]
                    if(a==0):
                        a=1
                    if(negativo):
                        a*=-1;
                    print("a = " + str(a))
                    del array[0]
                    del array[0]
                    del array[0]
                print(array)
# =============================================================================
#             identificazione operazione da "a"
# =============================================================================
                operazionedaa='+'
                if(len(array)>=2 and (array[0]=="+" or array[0]=="-")):
                    operazionedaa=array[0]
                    del array[0]
# =============================================================================
#             inizio calcolo di b
# =============================================================================
                operazionedab=operazionedaa
                b=0
                if("x" in array):
                    print("Esiste bx")
                    volta=0
                    negativo=False
                    if(array[0]=="(" and array[1]=="-"):
                        negativo=True
                        del array[0]
                        del array[0]
                    while(array[0]!="x"):
                        if(volta!=0):
                            b*=10;
                        volta+=1
                        b+=int(array[0]);
                        del array[0]
                    if(b==0):
                        b=1
                    if(negativo):
                        b*=-1
                    print("b = " + str(b))
                    del array[0]
                    if(array[0]==")"):
                        del array[0]
                    
                    if(len(array)>=2 and (array[0]=="+" or array[0]=="-")):
                        operazionedab=array[0]
                        del array[0]
# =============================================================================
#             inizio calcolo di c
# =============================================================================
                print(array)
                c=0
                if(len(array)>=1):
                    print("Esiste c")
                    volta=0
                    negativo=False
                    if(array[0]=="(" and array[1]=="-"):
                        negativo=True
                        del array[0]
                        del array[0]
                        del array[len(array)-1]
                        print(array)
                    print(array)
                    while(len(array)>0):
                        if(not volta==0):
                            c*=10;
                        volta+=1
                        c+=int(array[0]);
                        del array[0]
                    if(negativo):
                        c*=-1;
                    print("c = " + str(c))
                print(str(a) + "x^2" + str(operazionedaa) + str(b) + "x" + str(operazionedab) + str(c))
                
        elif(self.textDenominatore.text()=="0"):
            print("Denominatore: Error | ZeroDivision")
        else:
            print("Denominatore: Error | Empty")
        
        if(self.textX.text()!=""):
            x0=self.textX.text()
            print(x0)
            print("X(0): OK")
        else:
            print("X(0): Error | Empty")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    noLimit = QtWidgets.QMainWindow()
    ui = Ui_noLimit()
    ui.setupUi(noLimit)
    noLimit.show()
    sys.exit(app.exec_())

