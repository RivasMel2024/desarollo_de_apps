
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout
# Importamos el modulo donde esta instanciado el QColor
from layouts_colowidgets import Color

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        
        contenedor = QWidget()
        layout_contenedor = QHBoxLayout()

        columna1 = QWidget()
        layout1 = QVBoxLayout()

        columna2 = QWidget()
        layout2 = QVBoxLayout()

        columna3 = QWidget()
        layout3 = QVBoxLayout()
        
        
        layout1.addWidget(Color('lightgray'))
        layout1.addWidget(Color('khaki'))
        layout1.addWidget(Color('peru'))
        columna1.setLayout(layout1)
        layout_contenedor.addWidget(columna1)
        
        layout2.addWidget(Color('lightblue'))
        columna2.setLayout(layout2)
        layout_contenedor.addWidget(columna2)

        layout3.addWidget(Color('lightgreen'))
        layout3.addWidget(Color('lightcoral'))
        columna3.setLayout(layout3)
        layout_contenedor.addWidget(columna3)

        contenedor.setLayout(layout_contenedor)
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindows()
    window.show()
    app.exec()
