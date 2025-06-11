# Los widgets visuales son pushButton y Label. QWidget es un generico y QVBOxLayout es para ordenar los widgets

from PyQt6.QtWidgets import ( QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit, QCheckBox, QListWidget )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        self.widget = QListWidget() 
        self.widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)  # Permite seleccionar varios elementos
        self.widget.addItems(
            ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
            )
        self.widget.currentItemChanged.connect(self.item_cambiado) ## Cual es el ultimo item seleccionado
        self.widget.selectionModel().selectionChanged.connect(self.seleccion_cambiado)

        self.setCentralWidget(self.widget)

    def item_cambiado(self, item):
        print(item.text())

    def seleccion_cambiado(self):
        items_seleccionados = self.widget.selectedItems()
        print("Items seleccionados:")
        for item in items_seleccionados:
            print(item.text())
    

if __name__ == "__main__": 
    app = QApplication([]) ## Contenedor que administra los eventos
    window = MainWindow()
    window.show()
    app.exec()

        