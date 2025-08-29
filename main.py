import sys
 
from buttons import ButtonsGrid
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
    info = Info('')
    window.addWidgetToVLayout(info)
 
    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid
    buttonsGrid = ButtonsGrid(display,info, window)
    window.verticalLayout.addLayout(buttonsGrid)

    # Executa tudo
 
    window.show()
    app.exec()