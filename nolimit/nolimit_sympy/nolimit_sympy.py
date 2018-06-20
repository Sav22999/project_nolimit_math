## SOFTWARE SVILUPPATO DA SAVER1O MORELLI - LICENZA GNU V3 || Software developed by Saverio Morelli - GNU V3 License
## VERSIONE 1.6 - Version 1.6

from PyQt5 import uic, QtWidgets, QtGui
import sys
import os

from sympy import limit, lambdify, SympifyError
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_tokenize import TokenError
from sympy.plotting import plot

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

UI_FILE  = os.path.join(os.path.dirname(__file__), "./nolimit_sympy.ui")
textVersione="1.0β"

# import typing should add types


class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # initialize empty array for x and y
        self.x_val = np.arange( -100, 100, 0.1)
        self.y_val = np.empty((2000))

    def plot_sympy_expression(self, expr):

        x_lam = lambdify(x, expr, modules=["numpy"])
        self.y_val[:] = np.array(x_lam(self.x_val))

        self.axes.cla()
        self.axes.plot([min(self.x_val), -1, 0, 1, max(self.x_val)],[0, 0, 0, 0, 0], 'r', color='black')
        self.axes.plot([0, 0, 0, 0, 0],[min(self.y_val), -1, 0, 1, max(self.y_val)], 'r', color='black')
        self.axes.plot(self.x_val, self.y_val, 'r', color="red")
        self.draw()


class UiSympy(QtWidgets.QMainWindow, uic.loadUiType(UI_FILE)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.labelVersione.setText('<html><head/><body><p align="right"><span style="font-size:16px;color:white;background-color:darkred;">&nbsp;v'+textVersione+'&nbsp;</span></p></body></html>')

        self.plot_canvas = PlotCanvas(self)
        self.layout_plot.addWidget(self.plot_canvas)

        self.calculate.clicked.connect(self.do_calc)
        self.limit_expression.textChanged.connect(self.liveEdit)
        self.limit_value.textChanged.connect(self.liveEdit)
        self.show_details.clicked.connect(self.show_detailed_graph)
        self.calculate.setGeometry(10,350,341,61)
        self.show_details.hide()
        self.line_2.hide()

    def liveEdit(self):
        if self.liveCheck.isChecked():
            self.do_calc()

    def do_calc(self):
        try:
            expression = parse_expr(self.limit_expression.text())
            # check there is only Symbol('x') in the expression
            symbols = expression.free_symbols
            if symbols != {x} and symbols != set([]):
                raise SympifyError("Symbol allows is just the 'x'") # to go in except (!) not the best
            #  calculate the limit and plot
            result = limit(expression, x, self.limit_value.text())
            self.plot_canvas.plot_sympy_expression(expression)

            self.show_details.setEnabled(True)

            self.calculate.setGeometry(10, 270, 341, 61)
            self.show_details.show()
            self.line_2.show()
        except (SympifyError, SyntaxError, TokenError) as err:
            print(err)
            result = 'Error: Invalid input'
            #self.result.setTextColor(QtGui.QColor('red'))

        self.result.setText(str(result))

    def show_detailed_graph(self):
        expression = parse_expr(self.limit_expression.text())
        try:
            plot(expression)
        except TypeError:
            print("error during plot")
            QtWidgets.QMessageBox.warning(self, "plotting not supported",
                                              "the program does no support detailed plotting "
                                              "of a costant function! Please try with a different function")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UiSympy()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()