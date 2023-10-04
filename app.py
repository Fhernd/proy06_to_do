from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#@$MYSUPERSECRETKEY@#@$'

@app.route('/')
def index():
    return {
        'message': 'Hello World!'
    }
