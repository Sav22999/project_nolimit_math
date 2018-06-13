from PyQt5 import uic, QtWidgets, QtGui
import sys

from sympy import limit, lambdify, SympifyError, latex
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_tokenize import TokenError

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import unittest

UI_FILE = "main.ui"

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
        self.axes.plot(self.x_val, self.y_val, 'r', label=latex(expr))
        self.draw()
        self.axes.legend()


class uiSympy(QtWidgets.QMainWindow, uic.loadUiType(UI_FILE)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_canvas = PlotCanvas(self)
        self.layout_plot.addWidget(self.plot_canvas)

        self.calculate.clicked.connect(self.do_calc)
        self.limit_expression.textChanged.connect(self.do_calc)
        self.limit_value.textChanged.connect(self.do_calc)

    def do_calc(self):
        self.result.setTextColor(QtGui.QColor('black'))
        self.result.setText("")   # may not be very efficient

        try:
            expression = parse_expr(self.limit_expression.toPlainText())
            # check there is only Symbol('x') in the expression
            symbols = expression.free_symbols
            if symbols != set([x]) and symbols != set([]):
                raise SympifyError("symblos not allowed could use only x") # to go in except (!) not the best
            #  calculate the limit and plot
            result = limit(expression, x, self.limit_value.toPlainText())
            self.plot_canvas.plot_sympy_expression(expression)
        except (SympifyError, SyntaxError, TokenError) as err:
            print(err)
            result = 'error: invalid input'
            self.result.setTextColor(QtGui.QColor('red'))

        self.result.setText(str(result))


if __name__ == "__main__":
    print("per input mettere ** per elevare a potenza \n"
          "* per moltiplicazione \n"
          "oo per infinito")
    app = QtWidgets.QApplication(sys.argv)
    window = uiSympy()
    window.show()
    sys.exit(app.exec_())