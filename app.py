from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#@$MYSUPERSECRETKEY@#@$'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    datos = request.json
    return {'mensaje': 'Tarea almacenada correctamente'}
