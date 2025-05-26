# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        windowSize = QSize(900, 500)
        self.setFixedSize(windowSize)

        self.label1 = QLabel('Texto')
        self.label1.setFixedSize(300,200)
        self.label1.setScaledContents(True) # Es como un fit to windows
        # Creando una fuente como copia para modificarlo y sustituirlo con el original.
        fuente_label = self.label1.font() 

        self.label1.setPixmap(QPixmap('images\otje.jpg'))

        self.setCentralWidget(self.label1)
       

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        