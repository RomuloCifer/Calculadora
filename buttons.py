from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Display, Info


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
    def __init__(self, display: 'Display',info: 'Info', *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self._initial_equation = 'Sua conta'
        self._gridArray = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self._createGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self,value):
        self._equation = value

        self.info.setText(value)

    def _createGrid(self):
        for i, row in enumerate(self._gridArray):
            for j, text in enumerate(row):
                button = Button(text)
                if not isNumOrDot(button.text()) and not isEmpty(button.text()):
                    button.setProperty('specialButton', True)
                    self._configSpecialButton(button)
                self.addWidget(button, i, j)
                slot = self._makeSlot(self.insertButtonToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self,button,slot):
        button.clicked.connect(slot)
    
    def _configSpecialButton(self,button):
        text = button.text()
        if text == 'C':
            slot = self._makeSlot(self._clearDisplay)
            self._connectButtonClicked(button, slot)
        if text in '+-/*':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
            self._connectButtonClicked(button,self._makeSlot(self._eq, button)
            )

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def handler(_):
            func(*args, **kwargs)
        return handler
    
    def _clearDisplay(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._initial_equation
        return self.display.clear()
    
    def _operatorClicked(self,button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            print('nao fiz nada')
            return
        if self._left is None:
            self._left = float(displayText)
        self._operator = buttonText
        self.equation = f'{self._left} {self._operator} ??'
    
    def _eq(self,button):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        self._right = float(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        try:
            result = eval(self.equation)
            self.display.setText(str(result))
            self.info.setText(f'{self.equation} = {result}')
            self._left = result
            self._right = None
            self._operator = None

        except ZeroDivisionError:
            self.display.setText('Erro: Divisão por zero')
        except Exception as e:
            self.display.setText(f'Erro: {e}')
        self.display.clear()



    def insertButtonToDisplay(self, button):

        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText # type: ignore
        if not isValidNumber(newDisplayValue):
            if buttonText == 'C':
                self.display.setText('')  # type: ignore
            
        else:
            self.display.setText(newDisplayValue) # type: ignore
