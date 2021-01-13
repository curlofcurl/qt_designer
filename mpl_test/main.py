# ------------------------------------------------- -----
# ---------------------- main.py ------------------- ----
# --------------------------------------------- ---------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random


class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("qt_designer.ui", self)
        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")
        # self.pushButton_inputData.clicked.connect(self.onInputFileButtonClicked)
        # self.pushButton_inputData_2.clicked.connect(self.onInputFileButtonClicked)
        self.pushButton_inputData.clicked.connect(
            lambda le = self.lineEdit: self.onInputFileButtonClicked(self.lineEdit))

        self.pushButton_inputData_2.clicked.connect(
            lambda le = self.lineEdit_2: self.onInputFileButtonClicked(self.lineEdit_2))

        self.plotButton.clicked.connect(self.update_graph)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.fileList = []

    def onInputFileButtonClicked(self, lineedit):
        filename, filter = QFileDialog.getOpenFileName(None, caption='Open file')
        if filename:
            lineedit.setText(filename)
        self.fileList.append(filename)

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        self.MplWidget.canvas.axes.plot(t, sinus_signal)
        self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.MplWidget.canvas.axes.set_title(' Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

if __name__ == '__main__':
    app = QApplication([])
    window = MatplotlibWidget()
    window.show()
    app.exec_()
