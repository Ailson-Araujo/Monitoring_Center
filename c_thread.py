########################################################################
## MIT License
## Copyright © 2020, Ailson Software Development
##
## Autor: Ailson Araujo
## Versão: 1.0.0
## Data: 29/08/2020
##
## Este projeto pode ser usado livremente, desde que mantenham
## os respectivos créditos apenas nos scripts Python.
##
########################################################################
import time
from PyQt5.QtCore import QThread, pyqtSignal

class Pause(QThread):
    '''Emite um sinal apos o tempo declarado'''

    signal = pyqtSignal()

    def __init__(self, segundos):
        super(Pause, self).__init__()
        self.segundos = segundos

    def run(self):

        time.sleep(self.segundos)
        self.signal.emit()