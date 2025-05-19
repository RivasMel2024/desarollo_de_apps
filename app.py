
""" La mejor manera es crear subclases en donde esten todos los widgets """
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # se automatiza el proceso de instanciado 
        self.setWindowTitle("Mi primera app")
        self.setFixedSize(QSize(400, 300)) # tamaño fijo de la ventana
        # self.setMaximumSize(QSize(800, 600)) # tamaño maximo de la ventana
        # self.setMinimumSize(QSize(400, 300)) # tamaño minimo de la ventana

        # Sin self.button, button solo perteneceria a este metodo, 
        # al ponerlo como self, permitimos que los otros metodos puedan acceder a el
        self.button = QPushButton("Click me")
        self.button_width = 150
        self.button_height = 50
        self.button.setFixedSize(QSize(
            self.button_width, 
            self.button_height
        )) # tamaño fijo del boton
        self.button.setCheckable(True)
        self.estado_boton = True
        self.setCentralWidget(self.button)
    
        self.button.clicked.connect(self.button_clickeado) # click es una señal
        # self.button.clicked.connect(self.button_permanece_clikeado)
        self.button.setChecked(self.estado_boton) # estado inicial del boton

    def button_clickeado(self, clicked):
        """ Modificamos el comportamiento del boton """
        if clicked: 
            self.button.setText("Conectado")
            self.button_width += 10
            self.button_height += 5
            self.button.setFixedSize(QSize(
                self.button_width, 
                self.button_height
            ))
        else:
            self.button.setText("Desconectado")
        
        # self.button.hide() # cuando se hace click, el boton desaparece
            

    # def button_permanece_clikeado(self, clicked):
    #     print("Boton presionado?", clicked)

# Creamos la aplicacion
app = QApplication([]) # aqui es necesario que haya una lista, aunque sea vacia

window = MainWindow()


# Esto por si solo mostrara solo por un rato la ventana
window.show()
# Esto ayuda a mantener la ventana abierta, por medio de un bucle infinito   
app.exec()





""" Esta es la estructura base de una aplicacion QWidget"""
"""
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

# Creamos la aplicacion
app = QApplication([]) # aqui es necesario que haya una lista, aunque sea vacia

# Es el elemento visual
window = QWidget()

# Esto por si solo mostrara solo por un rato la ventana
window.show()
# Esto ayuda a mantener la ventana abierta, por medio de un bucle infinito   
app.exec()
"""

""" Esta es la estructura base de una aplicacion QMainWindow en vez de QApplication"""
"""
from PyQt6.QtWidgets import QApplication, QMainWindow

# Creamos la aplicacion
app = QApplication([]) # aqui es necesario que haya una lista, aunque sea vacia

window = QMainWindow()
window.setWindowTitle("Mi primera app")

# Esto por si solo mostrara solo por un rato la ventana
window.show()
# Esto ayuda a mantener la ventana abierta, por medio de un bucle infinito   
app.exec()
"""