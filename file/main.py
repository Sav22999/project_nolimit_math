## SOFTWARE SVILUPPATO DA SAVERIO MORELLI - LICENZA GNU V3
## VERSIONE 0.10

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random


def calcolaNumDen(testo, x0):
    print(testo)
    print(len(testo))
    array = list(testo)
    print(array)
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
        # print("c = " + str(c))
    print(str(a) + "x^2" + str(operazionedaa) + str(b) + "x" + str(operazionedab) + str(c))
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
        icon.addPixmap(QtGui.QPixmap("icona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.line.setGeometry(QtCore.QRect(85, 170, 320, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(403, -20, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textRisultato = QtWidgets.QLineEdit(self)
        self.textRisultato.setGeometry(QtCore.QRect(560, 10, 231, 32))
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
        #noLimit.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.plot = PlotCanvas(self, width=3.6, height=2.2)
        self.plot.move(430, 50)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("noLimit", "NoLimit Math v0.9 - by Saverio Morelli"))
        self.bttCalcola.setText(_translate("noLimit", "Calcola e\n"
                                                      "genera il grafico"))
        self.label.setText(_translate("noLimit", "lim"))
        self.label_2.setText(_translate("noLimit", "x→"))
        self.label_4.setText(_translate("noLimit",
                                        "<html><head/><body><p><img src=\"./icona.png\"/><span style=\" font-style:italic; color:#ff0000; vertical-align:super;\">Realizzato da Saverio Morelli</span></p></body></html>"))
        self.label_5.setText(_translate("noLimit",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; color:#ff0000;\">NoLimit Math</span></p></body></html>"))
        self.label_6.setText(_translate("noLimit", "Risultato:"))

        self.textDenominatore.setText("1")
        self.bttCalcola.clicked.connect(self.onClickCalcola)



    def onClickCalcola(self):
        numeratore = 1
        denominatore = 1
        x0 = 0

        if (self.textX.text() != ""):
            if (self.textX.text() != "inf"):
                x0 = float(self.textX.text())
                print("X(0): OK | Normal")
            else:
                print("X(0): OK | Infinite")
        else:
            print("X(0): Error | Empty")
        risultato = ''

        if (self.textNumeratore.text() != ""):
            print("Numeratore: OK")
            numeratore = calcolaNumDen(self.textNumeratore.text(), x0)
            # print(numeratore)
        else:
            print("Numeratore: Error | Empty")

        if (self.textDenominatore.text() != "" and self.textDenominatore.text() != "0"):
            if (self.textDenominatore.text() == "1"):
                print("Denominatore: OK | Static (1)")
            else:
                print("Denominatore: OK | Custom")
                denominatore = calcolaNumDen(self.textDenominatore.text(), x0)
                # print(denominatore)

        elif (self.textDenominatore.text() == "0"):
            print("Denominatore: Error | ZeroDivision")
        else:
            print("Denominatore: Error | Empty")

        if (denominatore != 0):
            if (numeratore != 0):
                risultato = numeratore / denominatore
        else:
            if (numeratore != 0):
                denDes = calcolaNumDen(self.textDenominatore.text(), (x0 + 0.1))
                # denSin=calcolaNumDen(self.textDenominatore.text(), (x0-0.1))
                self.textX.setText(self.textX.text() + "±")
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
        self.textRisultato.setText(str(risultato))

        #qui facendo
        #self.plot.plot(arrayX, arrayY,tipo_di_grafico, tutti i doc di matplot lib)
        #fai il grafico


class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
         self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_noLimit()
    ui.show()
    sys.exit(app.exec_())
