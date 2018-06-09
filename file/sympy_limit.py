from PyQt5 import uic, QtCore, QtWidgets
import sys
from sympy import limit, symbols, SympifyError
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


ui, _ = uic.loadUiType("sympy_limit.ui")
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


class Ui_sympy(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calculate.clicked.connect(self.do_calc)

    def do_calc(self):
        #must do input check
        x = symbols('x')
        try:
            result = limit(self.limit_expression.toPlainText(), x, self.limit_value.toPlainText())
        except SympifyError as err:
            print(err)
            result = 'error: ' + str(err)

        self.result.setText(str(result))

if __name__ == "__main__":
    print("per input mettere ** per elevare a potenza \n"
          "* per moltiplicazione \n"
          "oo per infinito")
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_sympy()
    window.show()
    sys.exit(app.exec_())