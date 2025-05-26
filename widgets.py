# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        self.label1 = QLabel('Texto')
        layout = QVBoxLayout()
        self.input1 =QLineEdit()
        self.input1.textEdited.connect(self.label1.setText) # Una accion dentro de otro widget
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        