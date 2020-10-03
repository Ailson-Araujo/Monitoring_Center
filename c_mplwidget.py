########################################################################
## Copyright © 2020 Ailson Araujo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## Versão: 1.0.0
## Iniciado: 29/08/2020
## Finalizado:
##
## Este projeto pode ser usado livremente, desde que mantenham
## os respectivos créditos nos scripts Python.
## Projeto feito com Qt Designer, PyQt5 e Matplotlib
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