from flask import Flask, render_template, request

from db.crud_todo import crear_tarea, eliminar_tarea, finalizar_tarea, obtener_tareas

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#@$MYSUPERSECRETKEY@#@$'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    todo = request.json
    
    resultado = crear_tarea(todo)
    
    if resultado:
        return {'mensaje': 'Tarea almacenada correctamente'}
    else:
        return {'mensaje': 'Error al almacenar la tarea'}


@app.route('/tareas', methods=['GET'])
def todas():
    tareas = obtener_tareas()
    return {'tareas': [tarea.__dict__ for tarea in tareas]}


@app.route('/tareas/<id>', methods=['DELETE'])
def eliminar(id):
    resultado = eliminar_tarea(id)
    
    if resultado:
        return {'mensaje': 'Tarea eliminada correctamente'}
    else:
        return {'mensaje': 'Error al eliminar la tarea'}


@app.route('/tareas/<id>', methods=['PUT'])
def modificar(id):
    resultado = finalizar_tarea(id)
    
    if resultado:
        return {'mensaje': 'Tarea finalizada correctamente'}
    else:
        return {'mensaje': 'Error al finalizar la tarea'}


@app.route('/tareas/todas', methods=['DELETE'])
def eliminar_finalizadas():
    tareas_ids = request.json
    tareas_ids = tareas_ids['tareasIds']
    
    for id in tareas_ids:
        resultado = eliminar_tarea(id)
    
    if resultado:
        return {'mensaje': 'Tareas eliminadas correctamente'}
    else:
        return {'mensaje': 'Error al eliminar las tareas'}
