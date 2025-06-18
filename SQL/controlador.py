# controlador.py 
# Es el que dirige todas las acciones de la aplicación.

import db # Importa tu módulo db.py (el Modelo)
columnas, datos = db.obtener_datos() # <--- La llamada a la DB ocurre AQUÍ, ¡antes de PyQt6!

from PyQt6.QtWidgets import QApplication # Necesario para la aplicación PyQt
import vista # Importa tu módulo vista.py (la Vista)

# El resto del código de iniciar_aplicacion() iría aquí, pero adaptado
# para usar 'columnas' y 'datos' que ya se obtuvieron.
# Necesitarías una función como esta:

def iniciar_aplicacion_con_datos(columnas_recibidas, datos_recibidos):
    app = QApplication([])
    main_view = vista.ArtistasView()

    if datos_recibidos:
        main_view.mostrar_artistas(columnas_recibidas, datos_recibidos)
    else:
        main_view.mostrar_mensaje_error("No se pudieron obtener los datos de los artistas. Verifique la conexión a la base de datos.")

    main_view.show()
    app.exec()

if __name__ == "__main__":
    # Llama a la nueva función con los datos ya obtenidos
    iniciar_aplicacion_con_datos(columnas, datos)