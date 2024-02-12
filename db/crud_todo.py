from datetime import datetime

from db.conexion import crear_conexion


def crear_tarea(tarea):
    """
    Crea una nueva tarea en la base de datos

    - tarea: str -- Descripción de la tarea
    """
    try:
        print('antes de crear conexion')
        conexion = crear_conexion()
        print('después de crear conexion')
        cursor = conexion.cursor()
        
        fecha_tarea = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fecha_modificacion = fecha_tarea
        print(fecha_tarea, fecha_modificacion)
        
        
        print('antes de execute')
        cursor.execute('INSERT INTO todo (Titulo, FechaTarea, TareaTerminada, FechaModificacion) VALUES (?, ?, ?, ?)', (tarea['titulo'], fecha_tarea, tarea['TareaTerminada'], fecha_modificacion))
        print('antes del commit')
        conexion.commit()
        print('después del commit')
        conexion.close()
        
        return True
    except Exception as e:
        print(e)
        return False
