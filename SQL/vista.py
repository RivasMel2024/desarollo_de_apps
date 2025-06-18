# vista.py
# Construye un contenedor con los resultados de las consultas SQL

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QScrollArea
)
from PyQt6.QtCore import Qt

class ArtistasView(QMainWindow):
    """
    Una vista PyQt6 para mostrar los datos de los artistas y mensajes.
    Ahora muestra artistas en QLabels dentro de un QVBoxLayout o QFormLayout.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chinook - Gestor de Artistas (Lista)")
        self.setGeometry(100, 100, 400, 600) # x, y, width, height

        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Etiqueta de título
        self.title_label = QLabel("Listado de Artistas")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(self.title_label)

        # --- Área de desplazamiento para mostrar la lista de artistas ---
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True) # Hace que el widget dentro del área de desplazamiento se redimensione
        
        # Contenedor para los artistas dentro del área de desplazamiento
        self.artists_container = QWidget()
        
        # Puedes elegir entre QVBoxLayout o QFormLayout
        self.artists_layout = QVBoxLayout(self.artists_container) # Opción 1: QVBoxLayout para listar simple
        # self.artists_layout = QFormLayout(self.artists_container) # Opción 2: QFormLayout para pares clave-valor

        self.scroll_area.setWidget(self.artists_container)
        main_layout.addWidget(self.scroll_area)
        # --- Fin del área de desplazamiento ---

        # Etiqueta para mensajes de estado o errores
        self.status_label = QLabel("Listo.")
        self.status_label.setStyleSheet("color: gray; font-size: 12px; margin-top: 5px;")
        main_layout.addWidget(self.status_label)

    def mostrar_artistas(self, columnas, datos):
        """
        Muestra los datos de los artistas usando QLabels dentro del layout.
        """

        if not datos:
            self.status_label.setText("ℹ️ No hay datos de artistas para mostrar.")
            return

        # Comprueba qué tipo de layout se está usando
        if isinstance(self.artists_layout, QVBoxLayout):
            for row_idx, row_data in enumerate(datos):
                artist_id = row_data[0]
                artist_name = row_data[1]
                
                # Crear un QLabel para cada artista
                artist_label = QLabel(f"{artist_id} - {artist_name}")
                artist_label.setStyleSheet("font-size: 14px; padding: 5px; border-bottom: 1px solid #eee;")
                self.artists_layout.addWidget(artist_label)
            
            # Añadir un "spacer" al final para que los elementos no se peguen arriba
            self.artists_layout.addStretch(1)

        self.status_label.setText(f"Mostrando {len(datos)} artistas.")

# --- Bloque de prueba para la vista PyQt6 ---
if __name__ == "__main__":
    print("--- Prueba del módulo vista.py (PyQt6 con Labels) ---") # Cambiado el nombre de prueba
    app = QApplication([])
    window = ArtistasView()

    # Ejemplo de uso con datos simulados
    columnas_ejemplo = ["ID de Artista", "Nombre del Artista"]
    datos_ejemplo = [
        (1, "AC/DC"),
        (2, "Accept"),
        (3, "Aerosmith"),
        (4, "Alanis Morissette"),
        (5, "Alice In Chains"),
        (6, "Antônio Carlos Jobim"),
        (7, "Apocalyptica"),
        (8, "Audioslave"),
        (9, "BackBeat"),
        (10, "Billy Cobham"),
    ]
    
    window.mostrar_artistas(columnas_ejemplo, datos_ejemplo)
    window.show()

    app.exec()
    print("---------------------------------")