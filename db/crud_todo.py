from datetime import datetime

from db.conexion import crear_conexion
from models.todo import Todo


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


# Obtiene todas las tareas de la base de datos:
def obtener_tareas():
    """
    Obtiene todas las tareas de la base de datos

    - returns: list -- Lista de tareas
    """
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        sql = 'SELECT * FROM todo'
        
        cursor.execute(sql)
        
        tareas = cursor.fetchall()
        
        tareas = [{'ID': tarea[0], 'Titulo': tarea[1], 'FechaTarea': tarea[2], 'TareaTerminada': tarea[3], 'FechaModificacion': tarea[4]} for tarea in tareas]
        
        tareas = [Todo(tarea['ID'], tarea['Titulo'], tarea['FechaTarea'], tarea['TareaTerminada'], tarea['FechaModificacion']) for tarea in tareas]
        
        conexion.close()
        
        return tareas
    except Exception as e:
        print(e)
        return None