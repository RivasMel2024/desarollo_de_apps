# db.py
# Aquí se conecta a la base de datos y obtiene los datos.
# Utiliza mysql-connector-python para conectarse a una base de datos MariaDB/MySQL


import mysql.connector
from mysql.connector import Error

def obtener_datos():
    try:

        # Se pasan los parámetros necesario para la conexión a la base de datos
        print("📡 Intentando conectar a la base de datos...")
        conexion = mysql.connector.connect(
            host='localhost',
            # port = 3306,  # Por defecto es 3306, pero puedes especificarlo si es diferente
            user='root',
            password='1234',
            database='chinook'
        )
        print("✅ Conectado correctamente.")

        # Es una instancia que me permite poder hacer consultas de tipo SQL
        cursor = conexion.cursor()
        print("🔍 Ejecutando consulta SQL...")
        cursor.execute("SELECT ArtistId, Name FROM artist LIMIT 25;")

        resultados = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]

        # Siempre hay que cerrar el cursor y la conexión después de usarlos, para eviar diferentes problemas
        print("🔒 Cerrando cursor y conexión...")
        cursor.close()
        conexion.close()

        print("📦 Datos obtenidos correctamente.")
        return columnas, resultados

    except Error as e:
        print("❌ Error al conectar a MariaDB")
        print(e)
        return [], []
