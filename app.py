from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '@#@$MYSUPERSECRETKEY@#@$'

@app.route('/')
def index():
    return render_template('index.html')
