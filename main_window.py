from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent : QWidget | None = None, *args, **kwargs) -> None :
        super().__init__(parent, *args,**kwargs)



        self.cw = QWidget()
        self.Vlayout = QVBoxLayout()
        self.cw.setLayout(self.Vlayout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle("Calculadora")

    def adjust_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(),self.height())
    
    def addWidgetToLayout(self,widget: QWidget):
        self.Vlayout.addWidget(widget)
        self.adjust_size()

