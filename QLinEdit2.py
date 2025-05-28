# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLineEdit, QSpinBox, QDoubleSpinBox )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # self.widget = QSpinBox() # No permite decimales
        self.widget = QDoubleSpinBox()

        self.widget.setEnabled(True)
        self.widget.setMinimum(-10)
        self.widget.setMaximum(15)
        self.widget.setSingleStep(0.25)
        self.widget.setPrefix("US$")
        # self.widget.setSuffix(".00")
        self.widget.valueChanged.connect(self.valor_cambiado)
        # self.widget.textChanged.connect(self.texto_cambiado)

        self.setCentralWidget(self.widget)
       
    def valor_cambiado(self, value):
        print(value)
        
    # def tabifiedDockWidgets(self):

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        