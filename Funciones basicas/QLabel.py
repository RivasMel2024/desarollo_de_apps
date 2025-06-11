# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        self.label1 = QLabel('Texto')

        # Creando una fuente como copia para modificarlo y sustituirlo con el original.
        fuente_label = self.label1.font() 
        fuente_label.setPointSize(30)
        fuente_label.setUnderline(True)

        self.label1.setFont(fuente_label)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label1)
       

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        