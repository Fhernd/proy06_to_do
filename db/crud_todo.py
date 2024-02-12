from datetime import datetime

from db.conexion import crear_conexion


def crear_tarea(tarea):
    """
    Crea una nueva tarea en la base de datos

    - tarea: str -- Descripción de la tarea
    """
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        tarea_terminada = 1 if tarea['terminada'] else 0
        fecha_tarea = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fecha_modificacion = fecha_tarea
        
        sql = 'INSERT INTO todo (Titulo, FechaTarea, TareaTerminada, FechaModificacion) VALUES (?, ?, ?, ?)'
        
        datos = (tarea['titulo'], fecha_tarea, tarea_terminada, fecha_modificacion)
        
        cursor.execute(sql, datos)
        
        conexion.commit()
        conexion.close()
        
        return True
    except Exception as e:
        print(e)
        return False
