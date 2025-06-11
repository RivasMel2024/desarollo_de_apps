
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout
# Importamos el modulo donde esta instanciado el QColor
from layouts_colowidgets import Color

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        layout =    QGridLayout()
        
        layout.addWidget(Color('lightgray'), 0, 0)
        layout.addWidget(Color('khaki'), 0, 1)
        layout.addWidget(Color('peru'), 0, 2)
        layout.addWidget(Color('lightblue'), 1, 0)
        layout.addWidget(Color('lightgreen'), 1, 1)
        layout.addWidget(Color('lightcoral'), 1, 2)  

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindows()
    window.show()
    app.exec()
