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

# define o valor na barra de progresso
class SetValueProgressBar():
    '''
    scale: 0 Temperatura
    scale: 1 Humidade
    '''
    def __init__(self, scale, value, label, widget):
        self.scale = scale
        self.value = value
        self.label = label
        self.widget = widget
        self.set_value()


    def set_value(self):

        color = self.color_scale(self.value, self.scale)
        value = int(self.value)

        # valor maximo para a progresse bar
        MAX_VALUE = 100

        # Formatação da label para temperatura
        if self.scale == 0:
            htmlText = """<p align="center"><span style=" font-size:50pt; color:{COLOR}">{VALUE}</span>
                        <span style=" font-size:55pt; vertical-align:super; color:{COLOR}">°</span></p>"""

        # Formatação da label para Humidade
        elif self.scale == 1:
            htmlText = """<p align="center"><span style=" font-size:50pt; color:{COLOR}">{VALUE}</span>
                        <span style=" font-size:40pt; vertical-align:super; color:{COLOR}">%</span></p>"""

        self.label.setText(htmlText.replace("{VALUE}", str(value)).replace("{COLOR}", color))

        # O valor de preenchimento da barra de progresso vai de 0 a 1
        # "progresse recebe o valor maximo - valor recebido / valor maximo"
        progress = (MAX_VALUE - value) / float(MAX_VALUE)
        stop_1 = str(progress - 0.003)
        stop_2 = str(progress)

        # interrompe o progresso ao chegar no valor maximo
        if value == MAX_VALUE:
            stop_1 = "1"
            stop_2 = "1"

        # Base da barra de Progresso
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        
        # Define novos valores para a base da barra de progresso
        # aplica a base no widget
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)
        self.widget.setStyleSheet(newStylesheet)

    # Define a cor para cada faixa de valores
    def color_scale(self, value, scale):

        if value <= 20:
            color_temp = "rgba(85, 170, 255, 255)"
            color_humd = "rgba(240, 30, 30, 255)"
        if value > 20 and value <= 40:
            color_temp = "rgba(30, 255, 45, 255)"
            color_humd = "rgba(255, 125, 30, 255)"
        if value > 40 and value <= 60:
            color_temp = "rgba(240, 240, 35, 255)"
            color_humd = "rgba(240, 240, 35, 255)"
        if value > 60 and value <= 80:
            color_temp = "rgba(255, 125, 30, 255)"
            color_humd = "rgba(30, 255, 45, 255)"
        if value > 80 and value <= 200:
            color_temp = "rgba(240, 30, 30, 255)"
            color_humd = "rgba(85, 170, 255, 255)"

        if  scale == 0:
            return color_temp
        elif scale == 1:
            return color_humd