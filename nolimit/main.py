## SOFTWARE SVILUPPATO DA SAVER1O MORELLI - LICENZA GNU V3 || Software developed by Saverio Morelli - GNU V3 License
## VERSIONE 1.4 - Version 1.4

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

ICON_PATH = os.path.join(os.path.dirname(__file__), "./icona.png")

if __name__ == "__main__":  # needed for more comfortable dev should remove
    from nolimit.sympy.nolimit_sympy import UiSympy
    version = "dev"
else:
    from .sympy.nolimit_sympy import UiSympy
    import nolimit
    version = nolimit.__version__


## TITOLO DEL PROGETTO CHE APPARE SULLA FINESTRA || Project title which is shows on top the window
titolo_progetto_finestra=f"NoLimit Math v{version} - by SM"

def calcolaNumDen(testo, x0, infinito):
    #print(testo)
    #print(len(testo))
    array = list(testo)
    #print(array)
    # inizio calcolo di "a"
    a = 0
    if ("x^2" in testo):
        # print("Esiste ax^2")
        volta = 0
        negativo = False
        if (array[0] == "-"):
            negativo = True
            del array[0]
        while (array[0] != "x"):
            if (volta != 0):
                a *= 10;
            volta += 1
            a += int(array[0]);
            del array[0]
        if (a == 0):
            a = 1
        if (negativo):
            a *= -1;
        # print("a = " + str(a))
        del array[0]
        del array[0]
        del array[0]
        if(infinito): return a
    # identificazione operazione da "a"
    operazionedaa = '+'
    if (len(array) >= 2 and (array[0] == "+" or array[0] == "-")):
        operazionedaa = array[0]
        del array[0]
    # inizio calcolo di b
    operazionedab = operazionedaa
    b = 0
    if ("x" in array):
        # print("Esiste bx")
        volta = 0
        negativo = False
        while (array[0] != "x"):
            if (volta != 0):
                b *= 10;
            volta += 1
            b += int(array[0]);
            del array[0]
        if (b == 0):
            b = 1
        if (negativo):
            b *= -1
        # print("b = " + str(b))
        del array[0]
        if (infinito): return b

        if (len(array) >= 2 and (array[0] == "+" or array[0] == "-")):
            operazionedab = array[0]
            del array[0]
    # inizio calcolo di c
    c = 0
    if (len(array) >= 1):
        # print("Esiste c")
        volta = 0
        negativo = False
        while (len(array) > 0):
            if (not volta == 0):
                c *= 10;
            volta += 1
            c += int(array[0]);
            del array[0]
        if (negativo):
            c *= -1;
        if (infinito): return c
        # print("c = " + str(c))
    #print(str(a) + "x^2" + str(operazionedaa) + str(b) + "x" + str(operazionedab) + str(c))
    a = a * (x0 ** 2)
    b = b * (x0)
    c = c
    if (operazionedaa == "+"):
        risultato = a + b
    else:
        risultato = a - b

    if (operazionedab == "+"):
        risultato += c
    else:
        risultato -= c
    return risultato;

def calcolaX0(self, x):
    x0=0.0
    if ("∞" not in x):
        x0 = float(x)
        print("X(0): OK | Normal")
    else:
        if (x == "+∞"):
            x0 = 9999
            print("X(0): OK | Infinite (positive)")
        elif (x == "-∞"):
            x0 = -9999
            print("X(0): OK | Infinite (negative)")
    return x0


class Ui_noLimit(QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("noLimit")
        self.resize(800, 354)
        self.setMaximumSize(QtCore.QSize(800, 354))
        self.setMinimumSize(QtCore.QSize(800, 354))
        self.setGeometry(50, 100, 800, 354)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ICON_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setObjectName("centralwidget")
        self.bttCalcola = QtWidgets.QPushButton(self)
        self.bttCalcola.setGeometry(QtCore.QRect(320, 280, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bttCalcola.setFont(font)
        self.bttCalcola.setObjectName("bttCalcola")
        self.textX = QtWidgets.QLineEdit(self)
        self.textX.setGeometry(QtCore.QRect(45, 190, 40, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textX.setFont(font)
        self.textX.setText("")
        self.textX.setObjectName("textX")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(25, 150, 58, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(14, 180, 58, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textNumeratore = QtWidgets.QLineEdit(self)
        self.textNumeratore.setGeometry(QtCore.QRect(90, 140, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textNumeratore.setFont(font)
        self.textNumeratore.setObjectName("textNumeratore")
        self.textDenominatore = QtWidgets.QLineEdit(self)
        self.textDenominatore.setGeometry(QtCore.QRect(90, 183, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textDenominatore.setFont(font)
        self.textDenominatore.setObjectName("textDenominatore")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(85, 177, 320, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(415, -20, 2, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textRisultato = QtWidgets.QLineEdit(self)
        self.textRisultato.setGeometry(QtCore.QRect(515, 10, 281, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textRisultato.setFont(font)
        self.textRisultato.setReadOnly(True)
        self.textRisultato.setObjectName("textRisultato")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 391, 91))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(120, 20, 271, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(425, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.bttVediGrafico = QtWidgets.QPushButton(self)
        self.bttVediGrafico.setGeometry(QtCore.QRect(610, 280, 180, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bttVediGrafico.setFont(font)
        self.bttVediGrafico.setObjectName("bttVediGrafico")
        self.bttVediGrafico.hide()
        self.bttSympy = QtWidgets.QPushButton(self)
        self.bttSympy.setGeometry(QtCore.QRect(10, 280, 180, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bttSympy.setFont(font)
        self.bttSympy.setObjectName("bttSympy")
        self.checkLive = QtWidgets.QCheckBox(self)
        self.checkLive.setGeometry(QtCore.QRect(10, 220, 180, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkLive.setFont(font)
        self.checkLive.setObjectName("checkLive")

        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.textX.raise_()
        self.textDenominatore.raise_()
        self.textNumeratore.raise_()
        self.textRisultato.raise_()
        self.bttCalcola.raise_()
        self.bttVediGrafico.raise_()
        self.bttSympy.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.checkLive.raise_()
        css_btt="QPushButton{background-color:white;color:darkred;border:2px solid darkred;border-radius:5px;font-family:Rockwell;} QPushButton:hover{background-color:darkred;color:white;} QPushButton:pressed{background-color:red;border:0px;}"
        self.bttCalcola.setStyleSheet(css_btt)
        self.bttSympy.setStyleSheet(css_btt)
        self.bttVediGrafico.setStyleSheet(css_btt)
        css_txt="QLineEdit{background-color:transparent;color:darkred;border:0px solid transparent;border-bottom:1px solid darkred;opacity:.7;font-family:Rockwell;} QLineEdit:focus{border-bottom:2px solid red;opacity:1;background-color:transparent;}"
        self.textRisultato.setStyleSheet(css_txt)
        self.textNumeratore.setStyleSheet(css_txt)
        self.textDenominatore.setStyleSheet(css_txt)
        self.textX.setStyleSheet(css_txt)
        self.line.setStyleSheet("background-color:black;")
        self.line_2.setStyleSheet("background-color:darkred;")
        css_label = "color:#ff0000;font-family:Rockwell;"
        self.label.setStyleSheet(css_label)
        self.label_2.setStyleSheet(css_label)
        self.label_4.setStyleSheet(css_label)
        self.label_5.setStyleSheet(css_label)
        self.label_6.setStyleSheet(css_label)
        self.checkLive.setStyleSheet("color:darkred;font-family:Rockwell;")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.plot_canvas = PlotCanvas(self, width=3.6, height=2.2)
        self.plot_canvas.move(430, 50)
        #self.plot_canvas.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("noLimit", titolo_progetto_finestra))
        self.bttCalcola.setText(_translate("noLimit", "Calculate and\n"
                                                      "generate the graph"))
        self.bttVediGrafico.setText(_translate("noLimit", "View the detailed\n"
                                               "graph"))
        self.bttSympy.setText(_translate("noLimit", "Use the\n"
                                                    "Sympy library"))
        self.label.setText(_translate("noLimit", "lim"))
        self.label_2.setText(_translate("noLimit", "x→"))
        self.label_4.setText(_translate("noLimit",
                                        "<html><head/><body><p><img src=\"./icona.png\"/><span style=\" font-style:italic; font-family:Rockwell; color:#ff0000; vertical-align:super; font-size:26pt;\">Realised by Saverio Morelli</span></p></body></html>"))
        self.label_5.setText(_translate("noLimit",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-family:Rockwell; color:#ff0000;\">NoLimit Math</span></p></body></html>"))
        self.label_6.setText(_translate("noLimit", "Result:"))

        self.checkLive.setText(_translate("noLimit", "\"Live calculation\""))

        self.textDenominatore.setText("1")
        self.bttCalcola.clicked.connect(self.onClickCalcola)
        self.bttVediGrafico.clicked.connect(self.onClickVediGrafico)
        self.bttSympy.clicked.connect(self.onClickSympy)

        self.textNumeratore.textChanged.connect(self.liveEdit)
        self.textDenominatore.textChanged.connect(self.liveEdit)
        self.textX.textChanged.connect(self.liveEdit)

    def liveEdit(self):
        if self.checkLive.isChecked():
            self.onClickCalcola()

    def onClickCalcola(self):
        numeratore = 0
        denominatore = 1
        x0 = 0
        risultato='-'
        stringaX=self.textX.text()
        if("+-" in stringaX): stringaX=stringaX.replace("+-", "±")
        if("-+" in stringaX): stringaX=stringaX.replace("-+", "∓")
        if("±" in stringaX): stringaX=stringaX.replace("±", "")
        if("∓" in stringaX): stringaX=stringaX.text().replace("∓", "")
        if(stringaX=="inf" or stringaX=="∞"): stringaX="+inf"
        if("inf" in stringaX): stringaX=stringaX.replace("inf", "∞")
        self.textX.setText(stringaX)

        if(stringaX!="" and self.textNumeratore.text()!="" and self.textDenominatore.text()!="" and self.textDenominatore.text()!="0"):
            css_txt = "QLineEdit{background-color:transparent;color:darkred;border:0px solid transparent;border-bottom:1px solid darkred;opacity:.7;font-family:Rockwell;} QLineEdit:focus{border-bottom:2px solid red;opacity:1;background-color: transparent;}"
            self.textX.setStyleSheet(css_txt)
            self.textNumeratore.setStyleSheet(css_txt)
            self.textDenominatore.setStyleSheet(css_txt)

            if (stringaX != ""):
                x0=calcolaX0(self, stringaX)
            risultato = '0'

            if("∞" not in self.textX.text()):
                if (self.textNumeratore.text() != ""):
                    print("Numerator: OK")
                    numeratore = calcolaNumDen(self.textNumeratore.text(), x0, False)
                    # print(numeratore)

                if (self.textDenominatore.text() != "" and self.textDenominatore.text() != "0"):
                    if (self.textDenominatore.text() == "1"):
                        print("Denominator: OK | Static (1)")
                    else:
                        print("Denominator: OK | Custom")
                        denominatore = calcolaNumDen(self.textDenominatore.text(), x0, False)
                        # print(denominatore)

                if (denominatore != 0):
                    if (numeratore != 0):
                        risultato = numeratore / denominatore
                else:
                    if (numeratore != 0):
                        denDes = calcolaNumDen(self.textDenominatore.text(), (x0 + 0.00001), False)
                        # denSin=calcolaNumDen(self.textDenominatore.text(), (x0 - 0.00001), False)
                        self.textX.setText(stringaX + "±")
                        if (denDes < 0):
                            if (numeratore < 0):
                                risultato = "±∞"
                            else:
                                risultato = "∓∞"
                        else:
                            if (numeratore > 0):
                                risultato = "±∞"
                            else:
                                risultato = "∓∞"
            else:
                if ("x^2" in self.textNumeratore.text()):
                    if ("x^2" in self.textDenominatore.text()):
                        aN = calcolaNumDen(self.textNumeratore.text(), x0, True)
                        aD = calcolaNumDen(self.textDenominatore.text(), x0, True)
                        risultato = aN / aD
                    else:
                        segnoNum=calcolaNumDen(self.textNumeratore.text(), x0, False)
                        segnoDen=calcolaNumDen(self.textDenominatore.text(), x0, False)
                        if(segnoNum>0 and segnoDen>0 or segnoNum<0 and segnoDen<0):
                            risultato = "+∞"
                        else:
                            risultato = "-∞"
                elif ("x" in self.textNumeratore.text()):
                    if ("x^2" in self.textDenominatore.text()):
                        segnoNum = calcolaNumDen(self.textNumeratore.text(), x0, False)
                        segnoDen = calcolaNumDen(self.textDenominatore.text(), x0, False)
                        risultato=0
                    elif ("x" in self.textDenominatore.text()):
                        bN = calcolaNumDen(self.textNumeratore.text(), x0, True)
                        bD = calcolaNumDen(self.textDenominatore.text(), x0, True)
                        risultato = bN / bD
                    else:
                        segnoNum = calcolaNumDen(self.textNumeratore.text(), x0, False)
                        segnoDen = calcolaNumDen(self.textDenominatore.text(), x0, False)
                        if (segnoNum > 0 and segnoDen > 0 or segnoNum < 0 and segnoDen < 0):
                            risultato = "+∞"
                        else:
                            risultato = "-∞"
                else:
                    if ("x^2" in self.textDenominatore.text() or "x" in self.textDenominatore.text()):
                        segnoNum = calcolaNumDen(self.textNumeratore.text(), x0, False)
                        segnoDen = calcolaNumDen(self.textDenominatore.text(), x0, False)
                        risultato=0
                    else:
                        cN = calcolaNumDen(self.textNumeratore.text(), x0, True)
                        cD = calcolaNumDen(self.textDenominatore.text(), x0, True)
                        risultato = cN / cD
            self.textRisultato.setText(str(risultato))
            
            valNum=self.textNumeratore.text()
            valDen=self.textDenominatore.text()
            """print("Numerator:")
            print(valDen)
            print("Denominator:")
            print(valDen)"""
            i = 0
            listX1=[]
            listX2=[]
            listY1=[]
            listY2=[]
            for count in range(0,100):
                try:
                    num = float(calcolaNumDen(valNum, (x0 + i), False) / calcolaNumDen(valDen, (x0 + i), False))
                    num = float(calcolaNumDen(valNum, (x0 - i), False) / calcolaNumDen(valDen, (x0 - i), False))
                except ZeroDivisionError:
                    i += 0.01
                listX1.append(x0 + i)
                listY1.append(calcolaNumDen(valNum, (x0 + i), False)/calcolaNumDen(valDen, (x0 + i), False))
                listX2.append(x0 - i)
                listY2.append(calcolaNumDen(valNum, (x0 - i), False)/calcolaNumDen(valDen, (x0 - i), False))
                if(x0==9999 or x0==-9999):
                    i += 100
                else:
                    i += 0.05
                
            # print(listX1)
            # print(listY1)
            # print(listX2)
            # print(listY2)
            self.plot_canvas.axes.cla()
            self.plot_canvas.axes.plot([min([min(listX1),min(listX2)]),-1,0,1,max([max(listX1),max(listX2)])], [0,0,0,0,0], 'r', color='black')
            self.plot_canvas.axes.plot([0,0,0,0,0], [min([min(listY1),min(listY2)]),-1,0,1,max([max(listY1),max(listY2)])], 'r', color='black')
            self.plot_canvas.axes.plot(listX1,listY1, 'r', color='red')
            self.plot_canvas.axes.plot(listX2,listY2, 'r', color='red')
            self.plot_canvas.draw()

            self.bttVediGrafico.show()
        else:
            css_txt = "QLineEdit{background-color:transparent;color:darkred;border:0px solid transparent;border-bottom:1px solid darkred;opacity:.7;font-family:Rockwell;} QLineEdit:focus{border-bottom:2px solid red;opacity:1;background-color: transparent;}"
            self.textX.setStyleSheet(css_txt)
            self.textNumeratore.setStyleSheet(css_txt)
            self.textDenominatore.setStyleSheet(css_txt)
            if stringaX=="":
                print("X(0): Error | Empty")
                self.textX.setStyleSheet(css_txt.replace("background-color:transparent;","background-color:red;"))
            if self.textNumeratore.text()=="":
                print("Numerator: Error | Empty")
                self.textNumeratore.setStyleSheet(css_txt.replace("background-color:transparent;", "background-color:red;"))
            if self.textDenominatore.text()=="":
                print("Denominator: Error | Empty")
                self.textDenominatore.setStyleSheet(css_txt.replace("background-color:transparent;", "background-color:red;"))
            if self.textDenominatore.text()=="0":
                print("Denominator: Error | ZeroDivision")
                self.textDenominatore.setStyleSheet(css_txt.replace("background-color:transparent;", "background-color:red;"))

    def onClickVediGrafico(self):
        stringaX = self.textX.text()
        if ("+-" in stringaX): stringaX = stringaX.replace("+-", "±")
        if ("-+" in stringaX): stringaX = stringaX.replace("-+", "∓")
        if ("±" in stringaX): stringaX = stringaX.replace("±", "")
        if ("∓" in stringaX): stringaX = stringaX.text().replace("∓", "")
        if (stringaX == "inf" or stringaX == "∞"): stringaX = "+inf"
        if ("inf" in stringaX): stringaX = stringaX.replace("inf", "∞")
        self.textX.setText(stringaX)
        if(stringaX!=""):
            x0 = calcolaX0(self, stringaX)
        valNum = self.textNumeratore.text()
        valDen = self.textDenominatore.text()
        i = 0
        listX1 = []
        listX2 = []
        listY1 = []
        listY2 = []
        for count in range(0, 1000):
            try:
                num = float(calcolaNumDen(valNum, (x0 + i), False) / calcolaNumDen(valDen, (x0 + i), False))
                num = float(calcolaNumDen(valNum, (x0 - i), False) / calcolaNumDen(valDen, (x0 - i), False))
            except ZeroDivisionError:
                i += 0.001
            listX1.append(x0 + i)
            listY1.append(calcolaNumDen(valNum, (x0 + i), False) / calcolaNumDen(valDen, (x0 + i), False))
            listX2.append(x0 - i)
            listY2.append(calcolaNumDen(valNum, (x0 - i), False) / calcolaNumDen(valDen, (x0 - i), False))
            if (x0 == 9999 or x0 == -9999):
                i += 50
            else:
                i += 0.005
        grafico_dettagliato=Grafico(self)
        grafico_dettagliato.setGrafico([min([min(listX1),min(listX2)]),-1,0,1,max([max(listX1),max(listX2)])], [0,0,0,0,0], 'r', 'black')
        grafico_dettagliato.setGrafico([0,0,0,0,0], [min([min(listY1),min(listY2)]),-1,0,1,max([max(listY1),max(listY2)])], 'r', 'black')
        grafico_dettagliato.setGrafico(listX1, listY1, 'r', 'red')
        grafico_dettagliato.setGrafico(listX2, listY2, 'r', 'red')
        grafico_dettagliato.showGrafico()


    def onClickSympy(self):
        self.sympy_window= UiSympy()
        self.sympy_window.show()



class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        ##self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    ##def compute_initial_figure(self):

class Grafico(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.showGrafico()

    def setGrafico(self, x, y, type, color):
        plt.plot(x, y, type, color=color)

    def showGrafico(self):
        plt.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_noLimit()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
