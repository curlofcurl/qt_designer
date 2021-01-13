#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random
from Graph import Mathpro, Graph

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
        try:
            filepath = self.lineEdit.text()

            f, t, Sxx = Mathpro.getSpectro(filepath)

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.pcolormesh(t, f, Sxx)
            self.MplWidget.canvas.axes.set_title('Spectrogram')
            self.MplWidget.canvas.draw()
        except:
            print('Something went wrong!  Please check the file data format.')

if __name__ == '__main__':
    app = QApplication([])
    window = MatplotlibWidget()
    window.show()
    app.exec_()
