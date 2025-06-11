# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLineEdit )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.widget = QLineEdit()
        self.widget.setMaxLength(10) # Solamente 10 caracteres
        self.widget.setPlaceholderText("Digite su nombre")
        self.widget.returnPressed.connect(self.presionar_enter)  
        # self.widget.textEdited.connect(self.editando_texto) 
        self.widget.textChanged.connect(self.texto_cambiado)

        self.setCentralWidget(self.widget)

    def presionar_enter(self):
        print("Se presiono Enter")
        self.widget.setText("Listo") # Se cambia el texto del widget, pero NO LO EDITA

    def editando_texto(self):
        print("Editando el texto")
                    
    def texto_cambiado(self, text):
        print(text)
    

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        