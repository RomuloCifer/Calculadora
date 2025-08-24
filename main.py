import sys
 
from buttons import Button
from components import Display, Info, MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH
 
if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
 
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
 
    # Info
    info = Info('Sua conta')
    window.addToVLayout(info)
 
    # Display
    display = Display()
    window.addToVLayout(display)
    # Display
    button = Button('oi')
    window.addToVLayout(button)

    # Grid
    # buttonsGrid = ButtonsGrid(display, info, window)
    # window.verticalLayout.addLayout(buttonsGrid)

    # Executa tudo
 
    window.show()
    app.exec()