from flask import Flask, render_template, request

from db.crud_todo import crear_tarea

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#@$MYSUPERSECRETKEY@#@$'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    datos = request.json
    
    resultado = crear_tarea(datos)
    
    if resultado:
        return {'mensaje': 'Tarea almacenada correctamente'}
    else:
        return {'mensaje': 'Error al almacenar la tarea'}
