# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit, QCheckBox )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        windowSize = QSize(900, 500)
        self.setFixedSize(windowSize)

        self.widget = QCheckBox("Aceptar")
        self.widget.setCheckState(Qt.CheckState.PartiallyChecked)
        self.widget.stateChanged.connect(self.mostrar_estado)

        self.setCentralWidget(self.widget)
       
    def mostrar_estado(self, estado):
        print("Si")
        # print(estado) # 0 - Unchecked, 1 - PartiallyChecked, 2 - Checked

        # Otra forma de mostrar el estado = sin argumentos
        print(self.widget.checkState().value)


if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        