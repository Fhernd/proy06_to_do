from conexion import crear_conexion


def crear_tarea(tarea):
    """
    Crea una nueva tarea en la base de datos

    - tarea: str -- Descripción de la tarea
    """
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO todo (Titulo, TareaTerminada) VALUES (?)', (tarea['titulo'], tarea['TareaTerminada']))
        conexion.commit()
        conexion.close()
        
        return True
    except Exception as e:
        return False
