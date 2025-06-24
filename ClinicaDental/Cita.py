from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton,
    QTextEdit, QGroupBox, QFormLayout, QMessageBox, QComboBox, QDateTimeEdit, QInputDialog, QScrollArea
)
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont
from datetime import datetime

class Cita:
    """
    Clase que representa una cita en la clínica dental.
    Contiene información sobre el paciente, el doctor, el horario y el estado de la cita.
    """
    def __init__(self, id_cita: str, paciente, doctor, hora_inicio: datetime, hora_fin: datetime, costo_cita: float):
        self.id_cita = id_cita                  # Identificador único de la cita
        self.paciente = paciente                # Paciente asociado a la cita
        self.doctor = doctor                    # Doctor asociado a la cita
        self.hora_inicio = hora_inicio          # Fecha y hora de inicio de la cita
        self.hora_fin = hora_fin                # Fecha y hora de fin de la cita
        self.costo_cita = costo_cita            # Costo de la cita
        self.estado = "Pendiente"               # Por defecto, la cita está pendiente

    def __str__(self):
        return (f"Cita{{id_cita='{self.id_cita}', "
                f"paciente={self.paciente.nombre} {self.paciente.apellido}, "
                f"doctor={self.doctor.nombre} {self.doctor.apellido}, "
                f"hora_inicio={self.hora_inicio}, hora_fin={self.hora_fin}, "
                f"estado='{self.estado}', costo_cita={self.costo_cita}}}")


class CitaWindow(QMainWindow):
    def __init__(self, doctores, pacientes, tratamientos):
        super().__init__()
        self.setWindowTitle("Gestión de Citas - Clínica Dental")
        self.setGeometry(100, 100, 900, 700)
        
        # Color scheme 
        self.colors = {
            'primary': '#130760',      # Dark blue-purple 
            'secondary': '#756f9f',    # Medium purple
            'accent': '#10b8b9',       # Teal
            'background': '#2b2b2b',   # Dark gray
            'surface': '#3c3c3c',      # Slightly lighter gray
            'text_light': '#ffffff',   # White text
            'text_dark': '#e0e0e0'     # Light gray text
        }

        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {self.colors['background']};
                font-family: 'Segoe UI';
                font-size: 14px;
                color: {self.colors['text_light']};
            }}
            
            QLabel {{
                color: {self.colors['text_light']};
                font-family: 'Segoe UI';
                font-size: 14px;
            }}
            
            QGroupBox {{
                font-family: 'Segoe UI';
                font-size: 14px;
                font-weight: bold;
                color: {self.colors['text_light']};
                border: 2px solid {self.colors['secondary']};
                border-radius: 8px;
                margin: 10px 0px;
                padding-top: 15px;
                background-color: {self.colors['surface']};
            }}
            
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                background-color: {self.colors['surface']};
                color: {self.colors['accent']};
            }}
            
            QLineEdit, QSpinBox, QDoubleSpinBox {{
                font-family: 'Segoe UI';
                font-size: 14px;
                border: 2px solid {self.colors['secondary']};
                border-radius: 6px;
                padding: 10px;
                background-color: {self.colors['surface']};
                color: {self.colors['text_light']};
                selection-background-color: {self.colors['accent']};
            }}
            
            QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {{
                border-color: {self.colors['accent']};
                background-color: #404040;
            }}
            
            QPushButton {{
                font-family: 'Segoe UI';
                font-size: 14px;
                font-weight: bold;
                color: {self.colors['text_light']};
                background-color: {self.colors['secondary']};
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                margin: 4px;
            }}
            
            QPushButton:hover {{
                background-color: {self.colors['accent']};
                
            }}
            
            QPushButton:pressed {{
                background-color: {self.colors['primary']};
            }}
            
            QTextEdit {{
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 13px;
                border: 2px solid {self.colors['secondary']};
                border-radius: 8px;
                background-color: {self.colors['surface']};
                color: {self.colors['text_dark']};
                padding: 15px;
                selection-background-color: {self.colors['accent']};
            }}
            
            QTextEdit:focus {{
                border-color: {self.colors['accent']};
            }}
        """)

        self.doctores = doctores
        self.pacientes = pacientes
        self.tratamientos = tratamientos
        self.citas = []

        self.editando_cita = None

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Creamos el scroll
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)
        self.setCentralWidget(scroll_area)

        # Título
        title = QLabel("📅 Gestión de Citas")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        main_layout.addWidget(title)

        # Información de la cita
        info_group = QGroupBox("Información de la Cita")
        info_layout = QFormLayout()

        self.id_edit = QLineEdit()
        self.paciente_combo = QComboBox()
        self.paciente_combo.addItems([f"{p['nombre']} {p['apellido']}" for p in self.pacientes])
        self.doctor_combo = QComboBox()
        for doctor in self.doctores:
            self.doctor_combo.addItem(str(doctor), doctor)  # str(doctor) usa el __str__ de la clase
        self.tratamiento_combo = QComboBox()
        self.tratamiento_combo.addItems([t['descripcion'] for t in self.tratamientos])

        self.fecha_inicio_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.fecha_inicio_edit.setDisplayFormat("dd/MM/yyyy HH:mm")
        self.fecha_fin_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.fecha_fin_edit.setDisplayFormat("dd/MM/yyyy HH:mm")
        self.costo_edit = QLineEdit()
        self.estado_combo = QComboBox()
        self.estado_combo.addItems(["Pendiente", "Confirmada", "Cancelada", "Asistida", "No asistió"])

        info_layout.addRow("ID Cita:", self.id_edit)
        info_layout.addRow("Paciente:", self.paciente_combo)
        info_layout.addRow("Doctor:", self.doctor_combo)
        info_layout.addRow("Tratamiento:", self.tratamiento_combo)
        info_layout.addRow("Fecha y Hora Inicio:", self.fecha_inicio_edit)
        info_layout.addRow("Fecha y Hora Fin:", self.fecha_fin_edit)
        info_layout.addRow("Costo:", self.costo_edit)
        info_layout.addRow("Estado:", self.estado_combo)

        info_group.setLayout(info_layout)
        main_layout.addWidget(info_group)

        # Botones
        buttons_layout = QHBoxLayout()
        self.crear_btn = QPushButton("➕ Crear Cita")
        self.crear_btn.clicked.connect(self.crear_cita)
        self.cancelar_btn = QPushButton("❌ Cancelar Cita")
        self.cancelar_btn.clicked.connect(self.cancelar_cita)
        self.modificar_btn = QPushButton("✏️ Modificar Cita")
        self.modificar_btn.clicked.connect(self.modificar_cita)
        self.confirmar_btn = QPushButton("✅ Confirmar Asistencia")
        self.confirmar_btn.clicked.connect(self.confirmar_asistencia)
        self.monto_btn = QPushButton("💲 Calcular Monto a Pagar")
        self.monto_btn.clicked.connect(self.calcular_monto)

        buttons_layout.addWidget(self.crear_btn)
        buttons_layout.addWidget(self.cancelar_btn)
        buttons_layout.addWidget(self.modificar_btn)
        buttons_layout.addWidget(self.confirmar_btn)
        buttons_layout.addWidget(self.monto_btn)
        main_layout.addLayout(buttons_layout)

        # Área de resultados
        self.resultado_text = QTextEdit()
        self.resultado_text.setReadOnly(True)
        self.resultado_text.setFont(QFont("Consolas", 13))
        self.resultado_text.setPlaceholderText("Aquí aparecerán los resultados de las operaciones...")
        main_layout.addWidget(self.resultado_text)

        self.setCentralWidget(central_widget)

    def crear_cita(self):
        """Crea una nueva cita verificando disponibilidad del doctor"""
        id_cita = self.id_edit.text().strip()
        paciente_idx = self.paciente_combo.currentIndex()
        doctor_idx = self.doctor_combo.currentIndex()
        tratamiento_idx = self.tratamiento_combo.currentIndex()
        hora_inicio = self.fecha_inicio_edit.dateTime().toPyDateTime()
        hora_fin = self.fecha_fin_edit.dateTime().toPyDateTime()
        costo = self.costo_edit.text().strip()
        estado = self.estado_combo.currentText()

        if not id_cita or paciente_idx == -1 or doctor_idx == -1 or tratamiento_idx == -1 or not costo:
            QMessageBox.warning(self, "❌ Error", "Todos los campos son obligatorios.")
            return

        # Verificar disponibilidad del doctor
        doctor = self.doctores[doctor_idx]
        for cita in self.citas:
            if cita.doctor == doctor and not (hora_fin <= cita.hora_inicio or hora_inicio >= cita.hora_fin):
                QMessageBox.warning(self, "❌ Error", "El doctor no está disponible en ese horario.")
                return

        paciente = self.pacientes[paciente_idx]
        tratamiento = self.tratamientos[tratamiento_idx]
        nueva_cita = Cita(id_cita, paciente, doctor, hora_inicio, hora_fin, float(costo))
        nueva_cita.tratamiento = tratamiento  # Puedes agregar este atributo dinámicamente
        nueva_cita.estado = estado

        self.citas.append(nueva_cita)
        self.resultado_text.append(f"Cita creada:\n{nueva_cita}")
        QMessageBox.information(self, "✅ Éxito", "Cita creada exitosamente.")
        self.limpiar_campos()

    def cancelar_cita(self):
        """Cancela una cita por ID"""
        id_cita, ok = QInputDialog.getText(self, "Cancelar Cita", "Ingrese el ID de la cita a cancelar:")
        if not ok or not id_cita.strip():
            return
        for cita in self.citas:
            if cita.id_cita == id_cita.strip():
                cita.estado = "Cancelada"
                self.resultado_text.append(f"Cita cancelada:\n{cita}")
                QMessageBox.information(self, "✅ Éxito", "Cita cancelada exitosamente.")
                return
        QMessageBox.warning(self, "❌ Error", "No se encontró la cita.")

    def modificar_cita(self):
        """Permite modificar fecha y hora de una cita"""
        id_cita, ok = QInputDialog.getText(self, "Modificar Cita", "Ingrese el ID de la cita a modificar:")
        if not ok or not id_cita.strip():
            return
        for cita in self.citas:
            if cita.id_cita == id_cita.strip():
                # Cargar datos actuales
                self.id_edit.setText(cita.id_cita)
                self.fecha_inicio_edit.setDateTime(QDateTime(cita.hora_inicio))
                self.fecha_fin_edit.setDateTime(QDateTime(cita.hora_fin))
                # El usuario puede modificar y luego presionar "Crear Cita" para guardar cambios
                self.editando_cita = cita
                QMessageBox.information(self, "Modificar Cita", "Modifique los campos y presione 'Crear Cita' para guardar cambios.")
                return
        QMessageBox.warning(self, "❌ Error", "No se encontró la cita.")

    def confirmar_asistencia(self):
        """Confirma si se asistió a la cita"""
        id_cita, ok = QInputDialog.getText(self, "Confirmar Asistencia", "Ingrese el ID de la cita:")
        if not ok or not id_cita.strip():
            return
        for cita in self.citas:
            if cita.id_cita == id_cita.strip():
                cita.estado = "Asistida"
                self.resultado_text.append(f"Asistencia confirmada:\n{cita}")
                QMessageBox.information(self, "✅ Éxito", "Asistencia confirmada.")
                return
        QMessageBox.warning(self, "❌ Error", "No se encontró la cita.")

    def calcular_monto(self):
        """Calcula el monto a pagar según el tipo de consulta y tratamiento"""
        id_cita, ok = QInputDialog.getText(self, "Calcular Monto", "Ingrese el ID de la cita:")
        if not ok or not id_cita.strip():
            return
        for cita in self.citas:
            if cita.id_cita == id_cita.strip():
                costo_cita = cita.costo_cita
                costo_tratamiento = getattr(cita, 'tratamiento', {}).get('costo', 0)
                total = costo_cita + costo_tratamiento
                self.resultado_text.append(
                    f"Monto a pagar para la cita {cita.id_cita}:\n"
                    f"Consulta: ${costo_cita:.2f}\n"
                    f"Tratamiento: ${costo_tratamiento:.2f}\n"
                    f"Total: ${total:.2f}\n"
                )
                QMessageBox.information(self, "Monto a Pagar", f"Total a pagar: ${total:.2f}")
                return
        QMessageBox.warning(self, "❌ Error", "No se encontró la cita.")

    def limpiar_campos(self):
        self.id_edit.clear()
        self.fecha_inicio_edit.setDateTime(QDateTime.currentDateTime())
        self.fecha_fin_edit.setDateTime(QDateTime.currentDateTime())
        self.costo_edit.clear()
        self.estado_combo.setCurrentIndex(0)
        self.paciente_combo.setCurrentIndex(0)
        self.doctor_combo.setCurrentIndex(0)
        self.tratamiento_combo.setCurrentIndex(0)

def main():
    # Debes pasar listas de doctores, pacientes y tratamientos reales aquí
    doctores = [{'nombre': 'Melisa', 'apellido': 'Rivas'}]
    pacientes = [{'nombre': 'Chris', 'apellido': 'Renderos'}]
    tratamientos = [{'descripcion': 'Limpieza', 'costo': 20.0}]
    app = QApplication([])
    window = CitaWindow(doctores, pacientes, tratamientos)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()