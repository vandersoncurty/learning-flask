from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return "ola mundo"

@app.route('/sobre')
def pag_sobre():
    return "sobre"

app.run(debug=True)