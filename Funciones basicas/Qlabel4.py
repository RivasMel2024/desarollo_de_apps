# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit, QCheckBox, QComboBox )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        widget = QComboBox()
        # widget.currentIndexChanged.connect(self.indice_cambio)
        widget.currentTextChanged.connect(self.texto_cambio)    
        widget.addItems(["Economia", "Derecho", "Ingenieria", "La mejor"])

        self.setCentralWidget(widget)

    def indice_cambio(self, i):
        print(i)

    def texto_cambio(self, t):
        print(t)
    

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        