from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber

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
    def __init__(self, display: QWidget, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.display = display
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
                button = Button(text)
                if not isNumOrDot(button.text()) and not isEmpty(button.text()):
                    button.setProperty('specialButton', True)
                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonConnection(self.insertButtonToDisplay, button)
                button.clicked.connect(buttonSlot)

    def _makeButtonConnection(self, func, *args, **kwargs):
        @Slot(bool)
        def handler(_):
            func(*args, **kwargs)
        return handler


    def insertButtonToDisplay(self, button):

        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText # type: ignore
        if not isValidNumber(newDisplayValue):
            if buttonText == 'C':
                self.display.setText('')  # type: ignore
            print('numero invalido')
        else:
            self.display.setText(newDisplayValue) # type: ignore
