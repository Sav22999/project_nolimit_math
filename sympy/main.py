from PyQt5 import uic, QtWidgets, QtGui
import sys
from sympy import limit, lambdify, SympifyError, symbols
from sympy.abc import x
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

UI_FILE = "main.ui"


ui, _ = uic.loadUiType("main.ui")
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


class Ui_sympy(QtWidgets.QMainWindow, uic.loadUiType(UI_FILE)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_canvas = PlotCanvas(self)
        self.layout_plot.addWidget(self.plot_canvas)

        self.calculate.clicked.connect(self.do_calc)
        self.limit_expression.textChanged.connect(self.do_calc)

    def do_calc(self):
        def do_plot(expression):
            x_val = np.arange( -100, 100, 0.1)
            x = symbols('x')
            x_lam = lambdify(x, expression, modules=["numpy"])
            y_val = x_lam(x_val)
            self.plot_canvas.axes.cla()
            self.plot_canvas.axes.plot(x_val, y_val, 'r')
            self.plot_canvas.draw()
            # plt.plot(x_val, y_val, 'r')
            # plt.show()
        #must do input check
        #clear text and color
        self.result.setTextColor(QtGui.QColor('black'))
        self.result.setText("")

        try:
            result = limit(self.limit_expression.toPlainText(), x, self.limit_value.toPlainText())
            do_plot(self.limit_expression.toPlainText())
        except (SympifyError) as err:
            print(err)
            result = 'error: invalid input'
            self.result.setTextColor(QtGui.QColor('red'))

        self.result.setText(str(result))

        # plotting
        # convert to numpy array


if __name__ == "__main__":
    print("per input mettere ** per elevare a potenza \n"
          "* per moltiplicazione \n"
          "oo per infinito")
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_sympy()
    window.show()
    sys.exit(app.exec_())