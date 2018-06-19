## SOFTWARE SVILUPPATO DA SAVER1O MORELLI - LICENZA GNU V3 || Software developed by Saverio Morelli - GNU V3 License
## VERSIONE 1.4 - Version 1.4

import sys
import os
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

UI_FILE  = os.path.join(os.path.dirname(__file__), "./nolimit.ui")
textVersione="1.0"

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


class Ui_noLimit(QtWidgets.QMainWindow, uic.loadUiType(UI_FILE)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.labelVersione.setText('<html><head/><body><p align="right"><span style="font-size:16px;color:white;background-color:darkred;">&nbsp;v'+textVersione+'&nbsp;</span></p></body></html>')

        self.plot_canvas = PlotCanvas(self)
        self.layout_plot.addWidget(self.plot_canvas)

        self.bttCalcola.clicked.connect(self.onClickCalcola)
        self.textNumeratore.textChanged.connect(self.liveEdit)
        self.textDenominatore.textChanged.connect(self.liveEdit)
        self.textX.textChanged.connect(self.liveEdit)
        self.bttVediGrafico.clicked.connect(self.onClickVediGrafico)
        self.bttCalcola.setGeometry(10,350,341,61)
        self.bttVediGrafico.hide()
        self.line_2.hide()

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
            self.bttCalcola.setGeometry(10, 270, 341, 61)
            self.bttVediGrafico.show()
            self.line_2.show()
                
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
    window = Ui_noLimit()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
