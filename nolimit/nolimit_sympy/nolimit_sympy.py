## SOFTWARE SVILUPPATO DA SAVER1O MORELLI - LICENZA GNU V3 || Software developed by Saverio Morelli - GNU V3 License
## VERSIONE - Version -> 1.0β

from PyQt5 import uic, QtWidgets, QtGui
import sys
import os

from sympy import limit, lambdify, SympifyError, N
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_tokenize import TokenError


import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


UI_FILE  = os.path.join(os.path.dirname(__file__), "./nolimit_sympy.ui")
textVersione="1.0.5β"

# import typing should add types


class MathExpression:
    """a wrapper around sympy expression for being able to use symbol which are not valid in sympy:
    -∞ or inf instead of oo
    -^ instead of **
    it returns also a substituted string.
    """
    replacements = {'∞': 'oo', 'inf': 'oo', '^': '**'}

    def __init__(self, expr):
        # replace expression
        expr = str(expr)
        for value, replacement in self.replacements.items():
            expr = expr.replace(value, replacement) # (!) not so efficient creates a new string every time

        # parse_expr from sympy.parsing.sympy_parser
        self.expr = parse_expr(expr)

    def __str__(self):
        expr_str = str(self.expr)
        for replacement, value in self.replacements.items():
            expr_str = expr_str.replace(value, replacement)
        return expr_str


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
        
        self.labelVersione.setText('<p align="right"><span style="font-size:16px;color:white;background-color:darkred;">&nbsp;v'+textVersione+'&nbsp;</span></p>')

        self.plot_canvas = PlotCanvas(self)
        self.layout_plot.addWidget(self.plot_canvas)
        self.expr = ""

        self.calculate.clicked.connect(self.do_calc)
        self.limit_expression.textChanged.connect(self.live_edit)
        self.limit_value.textChanged.connect(self.live_edit)
        self.show_details.clicked.connect(self.show_detailed_graph)
        self.resultFloat.stateChanged.connect(self.do_calc)
        self.calculate.setGeometry(10,350,341,61)
        self.show_details.hide()
        self.line_2.hide()


    def live_edit(self):
        if self.liveCheck.isChecked():
            self.do_calc()

    def do_calc(self):
        try:
            expression = MathExpression(self.limit_expression.text())
            # check there is only Symbol('x') in the expression
            symbols = expression.expr.free_symbols
            if symbols != {x} and symbols != set([]):
                raise SympifyError("Symbol allows is just the 'x'") # to go in except (!) not the best
            #  calculate the limit and plot
            result = MathExpression(limit(expression.expr, x, MathExpression(self.limit_value.text()).expr))
            if self.resultFloat.isChecked():
                result = N(result.expr)
            self.plot_canvas.plot_sympy_expression(expression.expr)

            self.show_details.setEnabled(True)

            self.calculate.setGeometry(10, 270, 341, 61)
            self.show_details.show()
            self.line_2.show()

            self.expr = expression.expr
        except (SympifyError, SyntaxError, TokenError) as err:
            result = 'Error: Invalid input'
            # if error hide show_details button
            self.calculate.setGeometry(10, 350, 341, 61)
            self.show_details.hide()
            self.line_2.hide()

        self.result.setText(str(result))
        if self.limit_value.text() in ['inf','∞','oo', '+inf', '+∞', '+oo']:
            self.limit_value.setText('+∞')
        elif self.limit_value.text() in ['-inf','-∞','-oo']:
            self.limit_value.setText('-∞')

    def show_detailed_graph(self):
        # (!) copied
        print(self.expr)
        x_val = np.arange(-10_000, 10_000)
        y_val = np.empty(20_000)
        x_lam = lambdify(x, self.expr, modules=["numpy"])
        y_val[:] = np.array(x_lam(x_val))

        plt.close()
        plt.plot([min(x_val), -1, 0, 1, max(x_val)], [0, 0, 0, 0, 0], 'r', color='black')
        plt.plot([0, 0, 0, 0, 0], [min(y_val), -1, 0, 1, max(y_val)], 'r', color='black')
        plt.plot(x_val, y_val, 'r', color="red")
        plt.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UiSympy()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()