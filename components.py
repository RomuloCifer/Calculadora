from PySide6.QtWidgets import QLineEdit, QLabel, QWidget, QMainWindow, QWidget, QVBoxLayout
from variables import *
from PySide6.QtCore import Qt

#display calculadora
#main window
class MainWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.centralWidg = QWidget()
        self.verticalLayout = QVBoxLayout(self.centralWidg)
        self.setCentralWidget(self.centralWidg)
        self.setWindowTitle("Calculadora")

    def addToVLayout(self, widget: QWidget):
        self.verticalLayout.addWidget(widget)

        self.adjustSize()


    def lock_size(self):
        self.adjustSize()
        self.setFixedSize(self.size())
        ###

class Display(QLineEdit):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setMinimumWidth(MINIMUM_WIDTH)

#info calculadora
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


