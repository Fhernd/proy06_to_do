import sqlite3


def crear_conexion():
    """
    Crea una conexion a la base de datos
    
    - returns: sqlite3.Connection -- Conexión a la base de datos
    """
    conexion = sqlite3.connect('db/todos.db')
    return conexion
