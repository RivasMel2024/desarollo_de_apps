# ---------------------------------------------------------------------
# Simulador de Sistema de Gestión de Pedidos Online Simplificado (GPOS)
# ---------------------------------------------------------------------
from PyQt6.QtWidgets import ( 
    QLabel, QApplication, QMainWindow, QPushButton, 
    QSpinBox, QWidget, QLineEdit, QFormLayout, QMessageBox, 
    QVBoxLayout, QHBoxLayout, QComboBox, 
    QSlider, QScrollArea )
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QDoubleValidator, QPixmap
import os
# ---------------------------------------------------------------------

# ===========================================
# Requisito Funcional: FR1.1
# Diccionario de usuarios para autenticación
# ===========================================

usuarios = {
    "melisa": "Qwerty123",
    "alisson": "ytrewQ321",
    "ale": "1234",
    "chris": "123Qwerty",
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador GPOS")
        self.setMinimumSize(QSize(800, 600))

        self.estado_imagenes = [ '1.png', 
                                 '2.png', 
                                 '3.png', 
                                 '4.png' 
                                ]

        contenedor = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(30, 20, 30, 20)

        lbl_titulo = QLabel("💻 Simulador de Gestión de Pedidos Online (GPOS) 🧮")
        lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        lbl_titulo.setContentsMargins(0, 20, 0, 20)
        self.main_layout.addWidget(lbl_titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        # =====================================
        # Requisito Funcional: FR1.1
        # Requisitos de Interfaz: UI1.1, UI1.4
        # Sección: Autenticación de Usuario
        # =====================================
        self.login_widget = QWidget()
        login_layout = QVBoxLayout()

        self.lbl_username = QLabel('Ingrese su nombre de usuario:')
        self.username = QLineEdit()
        self.username.setFixedWidth(200)

        username_container = QWidget()
        username_layout = QHBoxLayout()
        username_layout.setContentsMargins(20, 0, 20, 0)
        username_layout.setSpacing(5)
        username_layout.addWidget(self.lbl_username, alignment=Qt.AlignmentFlag.AlignLeft)
        username_layout.addWidget(self.username, alignment=Qt.AlignmentFlag.AlignLeft)
        username_container.setLayout(username_layout)

        self.lbl_password = QLabel('Ingrese su contraseña:')
        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.textChanged.connect(self.actualizar_estado_boton)

        password_container = QWidget()
        password_layout = QHBoxLayout()
        password_layout.setContentsMargins(20, 0, 20, 0)
        password_layout.setSpacing(5)
        password_layout.addWidget(self.lbl_password, alignment=Qt.AlignmentFlag.AlignLeft)
        password_layout.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignLeft)
        password_container.setLayout(password_layout)

        self.btn_login = QPushButton('Iniciar Sesión')
        self.btn_login.setFixedSize(QSize(200, 50))
        self.btn_login.clicked.connect(self.verificar_usuario)
                
        btn_container = QWidget()
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(0)
        btn_layout.addWidget(self.btn_login, alignment=Qt.AlignmentFlag.AlignCenter)
        btn_container.setLayout(btn_layout)
        
        login_layout.addWidget(username_container)
        login_layout.addWidget(password_container)
        login_layout.addWidget(btn_container, alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.setSpacing(10)

        self.login_widget.setLayout(login_layout)
        

        # =======================================
        # Requisito Funcional: FR1.2, F1.3
        # Requisitos de Interfaz: UI1.1, UI1.4
        # Sección: Seleccion de Producto y Stock
        # =======================================

        productos_widget = QWidget()
        productos_layout = QVBoxLayout()
        productos_layout.setSpacing(20)
        productos_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_productos = QHBoxLayout()
        self.lbl_articulo = QLabel('Articulo: Gadget X')
        info_productos.addWidget(self.lbl_articulo)
        
        cantidad_layout = QHBoxLayout()
        self.lbl_cantidad = QLabel('Cantidad: -')
        self.cantidad = QSpinBox()
        self.cantidad.setRange(0, 200)
        
        self.lbl_estado_stock = QLabel('Estado del Stock: En Stock')
        self.lbl_estado_stock.setStyleSheet('color: green;')
        self.stock_maximo = 150
        self.cantidad.valueChanged.connect(self.actualizar_estado_stock)
        self.cantidad.setEnabled(False)  

        cantidad_layout.addWidget(self.lbl_cantidad)
        cantidad_layout.addWidget(self.cantidad)
        info_productos.addLayout(cantidad_layout)
        info_productos.addWidget(self.lbl_estado_stock)

        productos_layout.addLayout(info_productos)
        productos_widget.setLayout(productos_layout)

        # =============================
        # Requisito Funcional: FR1.4
        # Requisitos de Interfaz: UI1.1
        # Sección: Datos de Contacto
        # =============================
        form_widget = QWidget()
        self.form_layout = QFormLayout()
        form_widget.setLayout(self.form_layout)
        
        # Formulario visible para todos los usuarios
        self.label1 = QLabel('Tipo de Cliente: Individual')

        self.form = QComboBox()
        self.form.addItems(['Individual', 'Empresa'])
        self.form.setFixedSize(150, 50)
        self.form.currentTextChanged.connect(self.identificador_usuario)
        self.form.setEnabled(False)

        self.label_nombre = QLabel("Ingrese su nombre completo")
        self.nombre = QLineEdit()
        self.nombre.setFixedWidth(300)
        self.nombre.setEnabled(False)

        self.form_layout.addRow(self.label1, self.form)
        self.form_layout.addRow(self.label_nombre, self.nombre)

        self.label_correo = QLabel("Ingrese su correo electronico")
        self.correo = QLineEdit()
        self.correo.setPlaceholderText("ejemplo@gmail.com")
        self.correo.setFixedWidth(300)
        self.correo.setEnabled(False)

        self.form_layout.addRow(self.label_correo, self.correo)

        # Formulario visible solo para empresas
        self.label_empresa = QLabel("Ingrese el nombre de su empresa")
        self.empresa = QLineEdit()
        self.empresa.setPlaceholderText("Ej: Monsters Inc.")
        self.empresa.setFixedWidth(300)

        self.label_ident = QLabel("Ingrese el nombre de su empresa")
        self.ident_fiscal = QLineEdit()
        self.ident_fiscal.setPlaceholderText("Ej: 0614-250185-102-3")
        self.ident_fiscal.setFixedWidth(300)
        
        # ======================================
        # Requisito Funcional: FR1.5
        # Requisitos de Interfaz: UI1.1
        # Sección: Resumen y Calculo de la Orden
        # ======================================
        resumen_widget = QWidget()
        resumen_layout = QVBoxLayout()

        self.lbl_precio_unitario = QLabel("Precio Unitario del Gadget X")
        self.precio_unitario = QLineEdit()
        self.precio_unitario.setFixedWidth(200)
        validador = QDoubleValidator(-9999.99, 9999.99, 2, self)
        validador.setNotation(QDoubleValidator.Notation.StandardNotation)        
        self.precio_unitario.setValidator(validador)
        self.precio_unitario.setEnabled(False)
        self.precio_unitario.textChanged.connect(self.actualizar_precio_unitario)

        self.lbl_porcentaje_cargo = QLabel("Porcentaje de Cargo por Servicio")
        self.porcentaje = QSlider(Qt.Orientation.Horizontal)
        self.porcentaje.setMaximum(0)
        self.porcentaje.setMaximum(100)
        self.porcentaje.setFixedWidth(200)
        self.porcentaje.setEnabled(False)

        self.lbl_porcentaje = QLabel("Porcentaje: 0%")
        self.porcentaje.valueChanged.connect(self.mostrar_porcentaje)

        form_layout = QFormLayout()
        form_layout.addRow(self.lbl_precio_unitario, self.precio_unitario)
        form_layout.addRow(self.lbl_porcentaje_cargo, self.porcentaje)
        form_layout.addRow(self.lbl_porcentaje, self.porcentaje)
        resumen_layout.addLayout(form_layout)

        self.lbl_monto_cargo = QLabel("Monto de Cargo por Servicio: $0.00")
        self.total_orden = QLabel("Total de la Orden: $0.00")
        self.porcentaje.valueChanged.connect(self.calculo_cuenta_final)
        self.cantidad.valueChanged.connect(self.calculo_cuenta_final)
        self.precio_unitario.textChanged.connect(self.calculo_cuenta_final)

        resumen_layout.addWidget(self.lbl_monto_cargo, alignment=Qt.AlignmentFlag.AlignCenter)
        resumen_layout.addWidget(self.total_orden, alignment=Qt.AlignmentFlag.AlignCenter)
        resumen_widget.setLayout(resumen_layout)
        
        # ====================================
        # Requisito Funcional: FR1.6
        # Requisitos de Interfaz: UI1.1, UI1.3
        # Sección: Estado General del Pedido
        # ====================================
        self.estado_pedido_widget = QWidget()
        estado_layout = QHBoxLayout()
        estado_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.estado_pedido = QSlider(Qt.Orientation.Horizontal)
        self.estado_pedido.setRange(0, 100)
        self.estado_pedido.setFixedWidth(300)
        self.estado_pedido.setEnabled(False)
        self.lbl_estado_pedido = QLabel("Estado: Pedido Inicial")
        self.valor = QLabel("0%")

        self.icono = QLabel('imagen')
        self.icono.setFixedSize(120, 120) 
        self.icono.setScaledContents(True)
        self.icono.setPixmap(QPixmap(r'imgs\1.png')) # modificar la ruta según sea necesario
        self.icono.setEnabled(False)

        self.estado_pedido.valueChanged.connect(self.actualizar_estado_pedido)

        estado_layout.addWidget(self.valor, alignment=Qt.AlignmentFlag.AlignCenter)
        estado_layout.addWidget(self.estado_pedido, alignment=Qt.AlignmentFlag.AlignCenter)
        estado_layout.addWidget(self.lbl_estado_pedido, alignment=Qt.AlignmentFlag.AlignCenter)
        estado_layout.addWidget(self.icono, alignment=Qt.AlignmentFlag.AlignCenter)
        self.estado_pedido_widget.setLayout(estado_layout)
        
        # ==============================
        # Requisito Funcional: FR1.7
        # Requisitos de Interfaz: UI1.1
        # Sección: Boton de Confirmación
        # ==============================

        self.confirmar_pedido = QPushButton('Confirmar Pedido')
        self.confirmar_pedido.setFixedSize(QSize(200, 50))
        self.confirmar_pedido.setEnabled(False)
        self.confirmar_pedido.clicked.connect(self.mensaje_confirmacion)

        self.nombre.textChanged.connect(self.actualizar_estado_boton)
        self.correo.textChanged.connect(self.actualizar_estado_boton)
        self.empresa.textChanged.connect(self.actualizar_estado_boton)
        self.ident_fiscal.textChanged.connect(self.actualizar_estado_boton)
        self.precio_unitario.textChanged.connect(self.actualizar_estado_boton)

        confirmar_container = QWidget()
        confirmar_layout = QHBoxLayout()
        confirmar_layout.setContentsMargins(0, 0, 0, 0)
        confirmar_layout.addWidget(self.confirmar_pedido)
        confirmar_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        confirmar_container.setLayout(confirmar_layout)


        ######################################
        # Anidando todos los layout y wigets #
        ######################################

        self.main_layout.addWidget(self.login_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(productos_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(form_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(resumen_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.estado_pedido_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(confirmar_container, alignment=Qt.AlignmentFlag.AlignCenter)
    
        contenedor.setLayout(self.main_layout)
        self.setCentralWidget(contenedor)

        # ============================
        # Scroll Area
        # ============================

        contenido = QWidget()
        contenido.setLayout(self.main_layout)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(contenido)

        self.setCentralWidget(scroll)

        # ===========================
        # Estilos y Paleta de Colores
        # ===========================
        self.login_widget.setStyleSheet(" background-color: #ccbba3; border-radius: 10px;")
        self.username.setStyleSheet("""
            QLineEdit {
                background-color: #f6f8f1;
                color: black;
                font-size: 14px;
                padding: 5px;
            }
        """)
        self.password.setStyleSheet("""
            QLineEdit {
                background-color: #f6f8f1;
                color: black;
                font-size: 14px;
                padding: 5px;
            }
        """)
        self.btn_login.setStyleSheet(
            """QPushButton {
                    background-color: #4f7d5d;
                    color: white;
                    border-radius: 10px;
                    padding: 10px;
                }"""
        )

        self.estado_pedido_widget.setStyleSheet(" background-color: #ccbba3; border-radius: 10px;")
        self.icono.setStyleSheet(" border-radius: 10px;")

        self.setStyleSheet("""
                QMainWindow {
                    background-color: #cee3d6;
                }
                QWidget {
                    background-color: #cee3d6;
                    color: white;
                }
                QLabel {
                    color: #1a3d2e;
                    font-family: 'Segoe UI';
                    font-size: 14px;
                    font-weight: 600;
                    
                }
                QLineEdit {
                    background-color: #f6f8f1;
                    color: black;
                    font-size: 14px;
                    padding: 5px;
                    border-radius: 10px;
                }
                QPushButton {
                    background-color: #4f7d5d;
                    color: white;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }
                QComboBox {
                    background-color: #f6f8f1;
                    color: black;
                    padding: 5px;
                }
                QSpinBox {
                    background-color: #f6f8f1;
                    color: black;
                    padding: 5px;
                }
                QComboBox {
                    background-color: #f6f8f1;
                    color: black;
                    padding: 5px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                QComboBox QAbstractItemView {
                    background-color: #fcf4e2;
                    color: black;
                    selection-background-color: #d7c6ac;
                    selection-color:  #1a3d2e;
                    border: 1px solid #ccc;
                }
                QMessageBox {
                    background-color: #fcf4e2;
                }
                QMessageBox QLabel {
                    background-color: #fcf4e2;
                    color: #1a3d2e;
                    font-family: 'Segoe UI';
                    font-size: 14px;
                }
                QMessageBox QPushButton {
                    color: white;
                    border-radius: 5px;
                    padding: 5px 15px;
                    min-width: 60px;
                }
                QMessageBox QPushButton:hover {
                    background-color: #ab9372;
                }
            """)

        


    # =====================================
    # Requisito Funcional: FR1.1
    # Sección: Autenticación de Usuario
    # =====================================
    def verificar_usuario(self):
        """Verifica las credenciales del usuario y permite el acceso al sistema."""
        usuario = self.username.text().lower()
        contrasena = self.password.text()

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"""Bienvenido {usuario.title()} al Simulador de Gestión de Pedidos Online (GPOS)."""
            QMessageBox.information(self, 'Bienvenido', mensaje)

            self.login_widget.hide()

            self.cantidad.setEnabled(True)
            self.confirmar_pedido.setEnabled(True)
            self.form.setEnabled(True)
            self.nombre.setEnabled(True)
            self.correo.setEnabled(True)
            self.precio_unitario.setEnabled(True)
            self.porcentaje.setEnabled(True)
            self.estado_pedido.setEnabled(True)
            self.icono.setEnabled(True)

            
            self.username.setEnabled(False)
            self.password.setEnabled(False)
            self.btn_login.setEnabled(False)
                    
        else:
            mensaje = """Credenciales incorrectas. Por favor, verifique su nombre de usuario y/o contraseña."""
            QMessageBox.warning(self, 'Error', mensaje)

    # =========================================
    # Requisito Funcional: FR1.2, F1.3
    # Sección: Seleccion de Producto y Stock
    # =========================================
    def actualizar_estado_stock(self):
        """Actualiza el estado del stock y la cantidad seleccionada."""

        cantidad = self.cantidad.value()
        self.lbl_cantidad.setText(f'Cantidad: {cantidad}')
        
        if cantidad > self.stock_maximo:
            self.lbl_estado_stock.setText('Estado del Stock: Sin Stock')
            self.lbl_estado_stock.setStyleSheet('color: red;')
        else:
            self.lbl_estado_stock.setText('Estado del Stock: En Stock')
            self.lbl_estado_stock.setStyleSheet('color: green;')
        
        self.actualizar_estado_boton()
    
    # =============================
    # Requisito Funcional: FR1.4
    # Sección: Datos de Contacto
    # =============================
    def identificador_usuario(self, tipo):
        """Actualiza el formulario según el tipo de usuario seleccionado."""
        if tipo == 'Empresa':
            self.form_layout.addRow(self.label_empresa, self.empresa)
            self.form_layout.addRow(self.label_ident, self.ident_fiscal)

            self.empresa.show()
            self.label_empresa.show()
            self.label_ident.show()
            self.ident_fiscal.show()

        elif tipo == 'Individual':
            self.empresa.hide()
            self.label_empresa.hide()
            self.label_ident.hide() 
            self.ident_fiscal.hide()
        
        self.actualizar_estado_boton()
        self.label1.setText(f"Tipo de empresa: {tipo}")
    
    # ======================================
    # Requisito Funcional: FR1.5
    # Sección: Resumen y Calculo de la Orden
    # ======================================
    def mostrar_porcentaje(self, value):
        """Actualiza el porcentaje de cargo por servicio y el texto correspondiente."""
        self.lbl_porcentaje.setText(f"Porcentaje: {value}%")
    
    def actualizar_precio_unitario(self, texto):
        """Actualiza el precio unitario del Gadget X y el total de la orden."""
        if texto:
           monto = float(texto)
           self.total_orden.setText(f"Total de la Orden: ${monto:,.2f}")
        else:
            self.lbl_precio_unitario.setText("Precio Unitario del Gadget X: $0.00")

    def calculo_cuenta_final(self):
        """Calcula el monto de cargo por servicio y el total de la orden."""
        try:
            porcentaje = self.porcentaje.value()
            precio_unitario = float(self.precio_unitario.text() or 0)
            cantidad = self.cantidad.value()
            subtotal = precio_unitario * cantidad
            monto_cargo = subtotal * (porcentaje / 100)
            total = cantidad * precio_unitario + monto_cargo

            self.lbl_monto_cargo.setText(f"Monto de Cargo por Servicio: ${monto_cargo:.2f}")
            self.total_orden.setText(f"Total de la Orden: ${total:.2f}")    
            
        except ValueError:
            self.lbl_monto_cargo.setText("Monto de Cargo por Servicio: $0.00")
            self.total_orden.setText("Total de la Orden: $0.00")

    # =============================================
    # Requisito Funcional: FR1.6
    # Sección: Seccion de Estado General del Pedido
    # =============================================
    def actualizar_estado_pedido(self, value):
        """Actualiza el estado del pedido y el icono según el valor del slider."""
        self.valor.setText(f"Valor {value}")
        # Modificar las rutas segun sea necesario
        if value == 0 :
            self.lbl_estado_pedido.setText("Nivel: Pedido Inicial")
            ruta = r'imgs\1.png'
        elif 1 <= value <= 30:
            self.lbl_estado_pedido.setText("Nivel: En proceso")
            ruta = r'imgs\2.png'
        elif 30 < value <= 70:
            self.lbl_estado_pedido.setText("Nivel: Pendiente de Aprobacion")
            ruta = r'imgs\3.png'
        elif 70 < value <= 100:
            self.lbl_estado_pedido.setText("Nivel: Pedido Finalizado")
            ruta = r'imgs\4.png'
        
        self.icono.setPixmap(QPixmap(ruta))

    # ==============================
    # Requisito Funcional: FR1.7
    # Requisitos de Interfaz: UI1.1
    # Sección: Boton de Confirmación
    # ==============================
    def verificar_campos_obligatorios(self):
        """Verifica que todos los campos obligatorios estén llenos y válidos."""
        # Validar campos básicos
        if not self.nombre.text() or not self.correo.text():
            return False
        
        # Validar campos de empresa
        if self.form.currentText() == 'Empresa':
            if not self.empresa.text() or not self.ident_fiscal.text():
                return False
            
        return True

    def es_contrasena_debil(self, contrasena):
        """Verifica si la contraseña cumple con los requisitos mínimos."""
        if len(contrasena) < 8:  # Mínimo 8 caracteres
            return True
        if not any(c.isupper() for c in contrasena):  # Al menos una mayúscula
            return True
        if not any(c.islower() for c in contrasena):  # Al menos una minúscula
            return True
        if not any(c.isdigit() for c in contrasena):  # Al menos un número
            return True
        return False

    def actualizar_estado_boton(self):
        """Actualiza el estado del botón según todas las condiciones requeridas."""
        campos_llenos = self.verificar_campos_obligatorios()
        stock_valido = self.cantidad.value() <= self.stock_maximo
        stock_selected = self.cantidad.value() > 0
        precio_valido = bool(self.precio_unitario.text())
        contrasena_fuerte = not self.es_contrasena_debil(self.password.text())
        
        self.confirmar_pedido.setEnabled(
            campos_llenos and 
            stock_valido and 
            precio_valido and
            stock_selected and
            contrasena_fuerte
        )

    def validar_formato_correo(self):
        """Valida que el formato del correo sea correcto."""
        correo = self.correo.text()
        return '@' in correo and '.' in correo

    def mensaje_confirmacion(self):
        """Muestra un mensaje de confirmación al usuario."""
        
        if self.cantidad.value() == 0:
            QMessageBox.warning(
                self, 
                "Error", 
                "Debe seleccionar una cantidad mayor a 0."
                )
            return

        # Validar formato de correo antes de continuar
        if not self.validar_formato_correo():
            QMessageBox.warning(
                self,
                "Error",
                "El formato del correo electrónico no es válido.\nDebe contener @ y un dominio válido (ejemplo@dominio.com)"
            )
            return
        
        tipo = self.form.currentText()
        mensaje = f"""
        Tipo de usuario: {tipo}
        Nombre completo: {self.nombre.text().title()}
        Correo electrónico: {self.correo.text()}
        Precio unitario del Gadget X: ${self.precio_unitario.text()}
        Cantidad: {self.cantidad.value()}
        Porcentaje de Cargo por Servicio: {self.porcentaje.value()}%
        Monto de Cargo por Servicio: ${self.lbl_monto_cargo.text().split('$')[1]}
        Total de la Orden: ${self.total_orden.text().split('$')[1]}
        Estado del Pedido: {self.lbl_estado_pedido.text()}
        """
        
        if tipo == "Empresa":
            mensaje += f"""
            Nombre de empresa: {self.empresa.text().title()}
            Identificación fiscal: {self.ident_fiscal.text()}
            """
        
        QMessageBox.information(
            self,
            "Resumen de Pedido",
            mensaje
        )



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()





