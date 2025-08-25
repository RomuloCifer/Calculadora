from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty

class Button(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(60,60)


class ButtonsGrid(QGridLayout):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self._gridArray = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self._createGrid()

    def _createGrid(self):
        for i, row in enumerate(self._gridArray):
            for j, text in enumerate(row):
                text = Button(text)
                if not isNumOrDot(text.text()) and not isEmpty(text.text()):
                    text.setProperty('specialButton', True)
                self.addWidget(text, i, j)
