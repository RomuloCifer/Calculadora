from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from main_window import MainWindow
import sys
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    #cria
    app = QApplication(sys.argv)
    window = MainWindow()
    #cria
    #icone#
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    #icone

    #tela
    window.show()
    #exec
    app.exec()
 