# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QWidget, QSlider, QHBoxLayout )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(900, 500))  
        # self.widget = QSpinBox() # No permite decimales
        self.widget = QSlider()
        self.widget.setOrientation(Qt.Orientation.Horizontal)   
        self.widget.setMinimum(-10)
        self.widget.setMaximum(10)
        self.widget.setSingleStep(2)

        self.label_valor = QLabel("Valor")
        self.label_estado = QLabel("Estado")

        contenedor = QWidget()
        layout = QHBoxLayout()

        layout.addWidget(self.label_valor)
        layout.addWidget(self.widget)
        layout.addWidget(self.label_estado)
        contenedor.setLayout(layout)

        self.widget.valueChanged.connect(self.valor_cambiado)
        self.widget.sliderPressed.connect(self.slider_presionado)
        self.widget.sliderReleased.connect(self.slider_presionado)

        self.setCentralWidget(contenedor)

    def valor_cambiado(self, value):
        self.label_valor.setText(f"Valor: {value}")

    def slider_presionado(self):
        estado_slider = self.widget.isSliderDown()
        if estado_slider:
            self.label_estado.setText("Deslizador presionado")
        else:
            self.label_estado.setText("Deslizador liberado")

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        