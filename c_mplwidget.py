########################################################################
## MIT License
## Copyright © 2020, Ailson Araujo.
##
## Autor: Ailson Araujo
## Versão: 1.0.0
## Iniciado: 29/08/2020
## Finalizado:
##
## Este projeto pode ser usado livremente, desde que mantenham
## os respectivos créditos apenas nos scripts Python.
## Projeto feito com Qt Designer e PyQt5
########################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.pyplot import Figure

class MplWidget(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvasQTAgg(Figure(figsize = (10, 10),
                                               dpi= 100,
                                               facecolor='#282c34',
                                               tight_layout=True))
        vertical_layout = QHBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.axes = self.canvas.figure.subplots()
        self.setLayout(vertical_layout)