from flask import Flask, render_template, request

from db.crud_todo import crear_tarea, obtener_tareas

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
